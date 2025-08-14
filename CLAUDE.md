# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a minimal LangChain workflow project built with Python 3.11+ and uv for dependency management. The application demonstrates basic conversational AI capabilities using OpenAI's GPT models through the LangChain framework.

## Development Commands

### Environment Management
- **Setup environment**: `uv sync`
- **Activate environment**: `source .venv/bin/activate` (Unix/Mac) or `.venv\Scripts\activate` (Windows)
- **Run application**: `uv run python main.py`

### Dependency Management
- **Add dependency**: `uv add package_name`
- **Add dev dependency**: `uv add --dev package_name`
- **View dependencies**: `cat pyproject.toml`

### Testing and Quality
- **Run application**: `uv run python main.py`
- **Test basic functionality**: Start the app and try a simple conversation

## Architecture & Structure

### Core Components
- **main.py**: Single-file application containing all workflow logic
- **Environment Configuration**: Uses python-dotenv for API key management
- **LangChain Workflow**: Simple prompt → model → parser chain using LCEL

### Key Functions
- `setup_environment()`: Loads environment variables from .env file
- `create_chat_model()`: Configures OpenAI ChatGPT model with API key validation
- `create_workflow()`: Builds the LangChain workflow using prompt templates and parsers
- `run_workflow()`: Executes the workflow with error handling
- `main()`: Interactive CLI loop for user conversations

### Dependencies
- **langchain**: Core framework for building LLM applications
- **langchain-openai**: OpenAI integration for LangChain
- **python-dotenv**: Environment variable management
- **LangChain Expression Language (LCEL)**: Used for chaining components with `|` operator

## Important Notes

### API Key Management
- Copy `.env.example` to `.env` and add your OpenAI API key
- The application will raise a ValueError if OPENAI_API_KEY is not set
- Never commit the `.env` file - it's included in .gitignore

### Development Guidelines
- Keep the application minimal and focused on demonstrating core LangChain concepts
- Use type hints for better code clarity
- Include docstrings for all functions
- Handle errors gracefully with user-friendly messages

### Extension Points
This minimal setup can be extended with:
- Memory management for conversation history
- Tool calling capabilities
- Vector stores for RAG (Retrieval Augmented Generation)
- Custom prompt templates
- Streaming responses
- Web interface integration