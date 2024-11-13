import pickle
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Load the pre-trained model and vectorizer
with open('sms_classifier_model.pkl', 'rb') as f:
    sms_classifier = pickle.load(f)

with open('sms_vectorizer.pkl', 'rb') as f:
    sms_vectorizer = pickle.load(f)

with open('email_classifier_model.pkl', 'rb') as f:
    email_classifier = pickle.load(f)

with open('email_vectorizer.pkl', 'rb') as f:
    email_vectorizer = pickle.load(f)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for SMS Spam detection
@app.route('/sms', methods=['POST'])
def sms_spam_detection():
    message = request.form['message']
    vectorized_message = sms_vectorizer.transform([message])
    prediction = sms_classifier.predict(vectorized_message)
    prediction_label = 'Spam' if prediction == 1 else 'Not Spam'
    return render_template('index.html', result=f'The SMS is: {prediction_label}')

# Route for Email Spam detection
@app.route('/email', methods=['POST'])
def email_spam_detection():
    message = request.form['message']
    vectorized_message = email_vectorizer.transform([message])
    prediction = email_classifier.predict(vectorized_message)
    prediction_label = 'Spam' if prediction == 1 else 'Not Spam'
    return render_template('index.html', result=f'The Email is: {prediction_label}')

if __name__ == '__main__':
    app.run(debug=True)
