# agentic-qa-tests-analyzer
This code uses the OpenAI SDK Agent Framework to implement an intelligent QA Agent. The QA Agent is responsible for reading and understanding application requirements, analyzing the target web application, reviewing the existing automated test suite, and evaluating the current test framework architecture.

Based on this analysis, the agent identifies test coverage gap and provides recommendations for improvements to the tests and the test framework.

The agent then generates a consolidated summary of all findings and recommendations in a file named test_recommendations.txt. In addition, it sends the recommendations via email in HTML format for easier review and distribution.

To accomplish these tasks, the QA Agent leverages a suite of custom Tools and configured MCP Servers that provide capabilities to format text, send email, use Playwright automation tool, read and write to specific folders. 
