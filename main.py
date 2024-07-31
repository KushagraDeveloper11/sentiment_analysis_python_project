import tkinter as tk
from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')

# Function to clear the text boxes
def reset_fields():
    url_entry.delete(0, tk.END)
    text_entry.delete(1.0, tk.END)
    result_label.config(text="")

# Function to perform sentiment analysis
def analyze_sentiment():
    url = url_entry.get()
    text = text_entry.get("1.0", tk.END)
    sentiment = None

    if url:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        text = article.summary

    if text.strip():
        blob = TextBlob(text)
        sentiment = round(blob.sentiment.polarity, 2)

    if sentiment is not None:
        if sentiment > 0.2:
            result_label.config(text="👍Very Happy😄", font=("Arial", 30), fg="green")
        elif sentiment < 0.2 and sentiment > 0.02:
            result_label.config(text="📈Mildly Happy😊", font=("Arial", 30), fg="lightblue")
        elif sentiment < -0.02 and sentiment > -0.2:
            result_label.config(text="📉Mildly Sad😞", font=("Arial", 30), fg="orange")
        elif sentiment < -0.2:
            result_label.config(text="👎Very Sad😢", font=("Arial", 30), fg="red")
        else:
            result_label.config(text="Neutral😐", font=("Arial", 30), fg="gray")
    else:
        result_label.config(text="Please enter a text to analyze", font=("Arial", 12), fg="black")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Sentiment Analyzer")
root.configure(bg="#f0f0f0")

# Welcome message
welcome_label = tk.Label(root, text="Welcome to the Sentiment Analyzer", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
welcome_label.pack(pady=10)

# URL entry
url_label = tk.Label(root, text="Enter URL of a news article:", bg="#f0f0f0", fg="#333333")
url_label.pack()
url_entry = tk.Entry(root, width=50, bg="#ffffff", fg="#333333", borderwidth=2, relief="groove")
url_entry.pack(pady=5)

# Text entry
text_label = tk.Label(root, text="Or paste your text below:", bg="#f0f0f0", fg="#333333")
text_label.pack()
text_entry = tk.Text(root, height=10, width=50, bg="#ffffff", fg="#333333", borderwidth=2, relief="groove")
text_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset_fields, bg="#d9534f", fg="#ffffff", font=("Arial", 12), borderwidth=0, padx=10, pady=5)
reset_button.pack(side=tk.LEFT, padx=10)

submit_button = tk.Button(button_frame, text="Submit", command=analyze_sentiment, bg="#5cb85c", fg="#ffffff", font=("Arial", 12), borderwidth=0, padx=10, pady=5)
submit_button.pack(side=tk.RIGHT, padx=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
