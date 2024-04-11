from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env.dev')

def ask_chatgpt(text):
    """
    Send a text to the ChatGPT API and return the result.

    Args:
        text (str): The text to send to the ChatGPT API.

    Returns:
        str: The response from ChatGPT.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    if not api_key:
        raise ValueError("The OPENAI_API_KEY is not set in the environment variables.")


    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",  # or use another model version
        messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                  {"role": "user", "content": text}])
        # Return the response text
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
