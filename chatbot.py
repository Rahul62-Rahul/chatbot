import nltk
import random
import string
import nltk.data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, wordpunct_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define a list of predefined responses
responses = {
    "greetings": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! What's up?"],
    "goodbye": ["Goodbye! Have a great day.", "Bye! Take care.", "See you later!"],
    "thanks": ["You're welcome!", "Happy to help!", "No problem!"],
    "default": ["Sorry, I didn't understand that. Can you rephrase?", "I'm not sure about that. Could you say it differently?"]
}

# Simple greeting detection
def respond_to_greeting(text):
    greetings = ['hello', 'hi', 'hey', 'greetings', 'morning', 'evening']
    text_tokens = word_tokenize(text.lower())
    for word in text_tokens:
        if word in greetings:
            return random.choice(responses["greetings"])
    return None

# Function to process text input and clean it
def clean_text(text):
    # Convert to lowercase, remove punctuation, and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    cleaned_words = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    return " ".join(cleaned_words)

# Default response function
def get_default_response():
    return random.choice(responses["default"])

# Function to process the user input and generate a response
def chat():
    print("ChatBot: Hello! I'm your assistant. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye! Take care.")
            break
        
        # Clean and process the input
        user_input_clean = clean_text(user_input)
        
        # Check for greetings
        greeting_response = respond_to_greeting(user_input)
        if greeting_response:
            print(f"ChatBot: {greeting_response}")
            continue
        
        # Default response for unrecognized queries
        print(f"ChatBot: {get_default_response()}")
        
# Start the chatbot
if __name__ == "__main__":
    chat()
