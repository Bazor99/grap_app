
# Advanced RAG LangGraph🦜🕸:


## Features

- **Refactored Notebooks**: The original LangChain notebooks have been refactored to enhance readability, maintainability, and usability for developers.
- **Production-Oriented**: The codebase is designed with a focus on production readiness, allowing developers to seamlessly transition from experimentation to deployment.
- **Test Coverage**: Comprehensive test coverage ensures the reliability and stability of the application, enabling developers to validate their implementations effectively.
- **Documentation**: Detailed documentation and branches guides developers through setting up the environment, understanding the codebase, and utilizing LangGraph effectively.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/langgraph-rag-app`

`OPENAI_API_KEY`

`TAVILY_API_KEY`

## Run Locally

Go to the project directory

```bash
  cd langgraph-rag-app
```

Install dependencies

```bash
  poetry install
```

Start the flask server

```bash
  poetry run main.py
```


## Running Tests

To run tests, run the following command

```bash
  poetry run pytest . -s -v
```
