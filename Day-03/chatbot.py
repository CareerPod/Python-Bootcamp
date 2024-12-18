from transformers import pipeline

# Initialize the pipeline with the correct task
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", ""]:
        print("Thanks for using this Chatbot!")
        break
    
    # Generate response
    response = chatbot(user_input, max_length=100, clean_up_tokenization_spaces=True)
    print("Chatbot:", response)