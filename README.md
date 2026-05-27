# agentic-qa
This code uses the OPENAI SDK  Agent framework.
The QA Agent will read the requirements, understand the web application, review the existing tests and test framework. Based on this it will analyze and provide recommendations on  tests coverage gap and test framework improvements. The agent will then create a summary of the recommendations in the file test_recommendations.txt and also send it via email.
Agent uses a suite of Tools and MCP Servers that have been setup to help accomplish its goal.
