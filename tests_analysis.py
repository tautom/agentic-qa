import asyncio
from contextlib import AsyncExitStack
import os
from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool, RunContextWrapper, Tool
from typing import Any
from agents.mcp import MCPServerStdio
import sendgrid
from typing import Dict
from sendgrid.helpers.mail import Mail, Email, To, Content
from IPython.display import Markdown, display
from datetime import datetime
from templates_qabot import *

load_dotenv(override=True)

# Custom tool to create directories and files under a specific dir path. 
@function_tool
def manage_filesystem(context: RunContextWrapper[Any], action: str, name: str, content: str = ""):
    """
    Creates a file or directory within the authorized workspace.
    
    Args:
        action: Either 'create_file' or 'create_dir'.
        name: The name of the file or directory.
        content: The text to write (only for files).
    """
    # Retrieve the restricted path from context
    base_path = context.context["base_path"]
    target_path = os.path.join(base_path, name)

    if action == "create_dir":
        os.makedirs(target_path, exist_ok=True)
        return f"Created directory: {name}"
    
    elif action == "create_file":
        with open(target_path, "w") as f:
            f.write(content)
        return f"Created file: {name}"



#Convert agent to tool for subject writer
subject_writer = Agent(name="Email subject writer", instructions=email_subject_instructions(), model="gpt-4o-mini")
subject_tool = subject_writer.as_tool(tool_name="subject_writer", tool_description="Write a subject for a cold sales email")

#Convert agent to tool for html formatting
html_converter = Agent(name="HTML email body converter", instructions=email_html_instructions(), model="gpt-4o-mini")
html_tool = html_converter.as_tool(tool_name="html_converter",tool_description="Convert a text email body to an HTML email body")

#Send email Tool
@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("<add your email here>")  # Change 
    to_email = To("add your email  here")  # Change to your recipient
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}

#Create agent to send emails
email_tools = [subject_tool, html_tool, send_email]
emailer_agent = Agent(
    name="Email Manager",
    instructions=email_instructions(),
    tools=email_tools,
    model="gpt-4o-mini",
    handoff_description="Convert an email to HTML format  and send it")


# Agent to analyze the existing tests. 
def create_agent_testsAnalyzer(server) -> Agent:
    qa_tools = [manage_filesystem]
    model= "gpt-5.4-mini"
    handoffs = [emailer_agent]
    qatester_agent = Agent(
        name="qatester agent", 
        instructions=qatester_instructions(),
        tools=qa_tools,
        model=model,
        mcp_servers=[server],
        handoffs=handoffs,
    )
    return qatester_agent

#Run agent to analyze the existing tests.
async def run_tests_analyzer():

    playwright_params = {"command": "npx","args": [ "@playwright/mcp@latest"]}
    async with AsyncExitStack() as stack:

        with trace("qatester_agent"):
            mcpserver = await stack.enter_async_context(MCPServerStdio(playwright_params, client_session_timeout_seconds=120))
            context_data = {"base_path": f"./{test_dir_path}"}
            os.makedirs(context_data["base_path"], exist_ok=True) 
            qatester_agent = create_agent_testsAnalyzer(mcpserver)
            result = await Runner.run(qatester_agent, qatester_message(), context=context_data, max_turns=30)
            display(Markdown(result.final_output))
        

if __name__ == "__main__":
    asyncio.run(run_tests_analyzer())
