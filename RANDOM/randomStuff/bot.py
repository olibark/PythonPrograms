import random
import nltk
from transformers import pipeline

# Download NLTK data (only required once)
nltk.download("punkt")

# Simple rule-based responses
def rule_based_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm just a computer program, but I'm doing fine!", "I'm great, thank you!"],
        "bye": ["Goodbye!", "See you later!", "Bye for now!"]
    }
    for key in responses.keys():
        if key in user_input.lower():
            return random.choice(responses[key])
    return None

# Advanced AI-based responses using Hugging Face's Transformers
def advanced_response(user_input):
    generator = pipeline("text-generation", model="gpt2")
    response = generator(user_input, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]

# Main chatbot loop
def chatbot():
    print("AI Chatbot: Hi! I'm your AI chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "quit":
            print("AI Chatbot: Goodbye!")
            break
        
        # Try rule-based response first
        response = rule_based_response(user_input)
        
        if response:
            print("AI Chatbot:", response)
        else:
            # Fallback to AI-based response
            print("AI Chatbot (AI Response):", advanced_response(user_input))

# Run the chatbot
chatbot()
