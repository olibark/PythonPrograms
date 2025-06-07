import os
import requests

# API endpoint for DeepSeek's public model hosted on Hugging Face
API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-llm-7b-instruct"

# Read the Hugging Face token from the environment, if provided
HF_TOKEN = os.getenv("HF_TOKEN")
headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}


def query(prompt: str) -> str:
    """Send a prompt to the model and return the generated text."""
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list) and data:
        # Hugging Face Inference API for text-generation returns a list of dicts
        return data[0].get("generated_text", "")
    # Fallback in case of error or unexpected response
    return str(data)


def main() -> None:
    print("DeepSeek Terminal Chat")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        try:
            output = query(user_input)
            print(f"AI: {output}\n")
        except requests.HTTPError as err:
            print(f"Request failed: {err}\n")
        except Exception as ex:
            print(f"Error: {ex}\n")


if __name__ == "__main__":
    main()
