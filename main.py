#!/usr/bin/env python3
"""
Minimal LangChain workflow application.

This demonstrates a basic conversational AI workflow using LangChain with OpenAI.
"""

import os
from typing import Dict, Any, Union

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def setup_environment() -> None:
    """Load environment variables from .env file."""
    load_dotenv()


def create_chat_model() -> Union[ChatOpenAI, ChatOllama]:
    """Create and configure the chat model (OpenAI or Ollama)."""
    # Check if Ollama is configured
    use_ollama = os.getenv("USE_OLLAMA", "false").lower() == "true"
    
    if use_ollama:
        # Use Ollama
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")
        
        return ChatOllama(
            model=ollama_model,
            base_url=ollama_base_url,
            temperature=0.7
        )
    else:
        # Use OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required when not using Ollama")
        
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=api_key
        )


def create_workflow() -> Any:
    """Create a simple conversational workflow using LangChain."""
    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Provide clear and concise responses."),
        ("human", "{input}")
    ])
    
    # Create chat model
    model = create_chat_model()
    
    # Create output parser
    output_parser = StrOutputParser()
    
    # Chain components together using LCEL (LangChain Expression Language)
    workflow = prompt | model | output_parser
    
    return workflow


def run_workflow(workflow: Any, user_input: str) -> str:
    """Execute the workflow with user input."""
    try:
        response = workflow.invoke({"input": user_input})
        return response
    except Exception as e:
        return f"Error: {str(e)}"


def main() -> None:
    """Main application entry point."""
    setup_environment()
    
    # Display which model is being used
    use_ollama = os.getenv("USE_OLLAMA", "false").lower() == "true"
    if use_ollama:
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")
        print(f"🤖 LangChain Workflow Demo (using Ollama: {ollama_model})")
    else:
        print("🤖 LangChain Workflow Demo (using OpenAI)")
    
    print("Type 'quit' to exit\n")
    
    try:
        workflow = create_workflow()
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            print("🤖 Assistant:", end=" ")
            response = run_workflow(workflow, user_input)
            print(response)
            print()
            
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"Application error: {e}")


if __name__ == "__main__":
    main()
