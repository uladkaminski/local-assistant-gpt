from openai import OpenAI
import ollama
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env.dev')

def ask_llm(text, api_choice='openai'):
    """
    Send a text to the chosen API (ChatGPT or Ollama) and return the result.

    Args:
        text (str): The text to send to the API.
        api_choice (str): The API to use ('openai' or 'ollama').

    Returns:
        str: The response from the API.
    """
    if api_choice == 'openai':
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("The OPENAI_API_KEY is not set in the environment variables.")
        client = OpenAI(api_key=api_key)

        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                      messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                                {"role": "user", "content": text}])
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"An error occurred with OpenAI: {e}")
            return None

    elif api_choice == 'ollama':
        try:
            response = ollama.chat(model='llama2', messages=[{"role": "user", "content": text}])
            return response['message']['content'].strip()
        except Exception as e:
            print(f"An error occurred with Ollama: {e}")
            return None

    else:
        raise ValueError("Invalid API choice. Please choose 'openai' or 'ollama'.")

# Example usage:
# result = ask_model("Hello, how are you?", "ollama")
# print(result)
