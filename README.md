# agentic-qa-tests-analyzer

`agentic-qa-tests-analyzer` is an intelligent QA analysis agent built using the OpenAI SDK Agent Framework.

The agent is designed to analyze requirements, Application Under Test, existing automated tests, and the supporting test automation framework in order to identify test coverage gaps and recommend improvements.

---

## Features

The QA Agent performs the following tasks:

* Reads and understands application requirements
* Analyzes the target web application
* Reviews existing automated test suites
* Evaluates the current test automation framework
* Identifies:

  * Test coverage gaps
  * Missing scenarios
  * Weaknesses in framework architecture
  * Opportunities for maintainability and scalability improvements
* Generates a consolidated recommendation report
* Sends recommendations via HTML email

---

## Output

The agent generates:

* `test_recommendations.txt`

  * Contains a summary of findings and recommendations

Additionally, the recommendations are emailed in HTML format for easier sharing and review.

---

## Tools and MCP Servers

The QA Agent leverages a suite of custom Tools and configured MCP Servers that provide capabilities such as:

* Text formatting
* Email delivery
* Playwright browser automation
* File system read/write operations
* Test and application analysis

---

## Prerequisites

Before running the project, ensure the following are installed/configured:

### 1. Install `uv` Package Manager

### 2. Configure Environment Variables

Create a `.env` file in the project root and add the required API keys and configuration values.

Example:

```env
OPENAI_API_KEY=your_api_key
SENDGRID_API_KEY=your_email_key
```

---


## Running the Agent

Execute the QA analysis agent using:

```bash
uv run tests_analysis.py
```

---

## Example Workflow

1. Agent reads application requirements
2. Agent analyzes the target web application
3. Existing tests and framework are reviewed
4. Coverage gaps and improvements are identified
5. Recommendations are written to:

   * `test_recommendations.txt`
6. HTML summary email is sent

---

## Technology Stack

* OpenAI SDK Agent Framework
* Python
* Playwright
* MCP Servers
* uv Package Manager

---

## Future Enhancements

Potential future improvements include:

* RAG
* MCP servers to connect to tools like Jira, Asana etc to read and review specs/requirements. 


---

## License

MIT License
