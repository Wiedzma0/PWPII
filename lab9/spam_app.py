import gradio as gr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dane treningowe (prosty przykład)
texts = ["Win money now", "Cheap loans available", "Hi, how are you?", "Meeting at 10", "Buy now!", "Free vacation"]
labels = ["spam", "spam", "ham", "ham", "spam", "spam"]

# Trenowanie modelu
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

def classify_email(email_text):
    vect = vectorizer.transform([email_text])
    prediction = model.predict(vect)[0]
    return f"To jest: {prediction.upper()}"

# Gradio UI
interface = gr.Interface(fn=classify_email, inputs="text", outputs="text", title="Spam Detector")
interface.launch()
