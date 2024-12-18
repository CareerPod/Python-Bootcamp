from transformers import pipeline

# Load a pre-trained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Input from the user
text = input("Enter a sentence: ")

# Perform sentiment analysis
result = classifier(text)

# Display the result
print(f"Sentiment: {result[0]['label']}, Confidence: {result[0]['score']:.2f}")