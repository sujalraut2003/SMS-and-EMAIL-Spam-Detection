import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle

# Function to load and process data
def load_and_train(file_path, model_path, vectorizer_path):
    # Load the dataset from the CSV file
    df = pd.read_csv(file_path)
    
    # Print column names to check if 'Label' and 'Message' are present
    print(f"Columns in {file_path}: {df.columns}")
    
    # Check if the columns 'Label' and 'Message' exist, if not, rename them
    if 'Label' not in df.columns or 'Message' not in df.columns:
        print(f"Renaming columns for {file_path} to ['Label', 'Message']")
        # Renaming columns, adjust as necessary based on inspection
        if len(df.columns) == 2:
            df.columns = ['Label', 'Message']
        else:
            raise ValueError(f"The input file {file_path} must contain 'Label' and 'Message' columns.")

    # Encode the labels (spam = 1, ham = 0)
    label_encoder = LabelEncoder()
    df['Label'] = label_encoder.fit_transform(df['Label'])

    # Split the dataset into features and labels
    X = df['Message']  # Features (SMS or Email messages)
    y = df['Label']    # Labels (spam or ham)

    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Convert the text data into numeric vectors using CountVectorizer
    vectorizer = CountVectorizer(stop_words='english')
    X_train_vect = vectorizer.fit_transform(X_train)
    X_test_vect = vectorizer.transform(X_test)

    # Train a Naive Bayes classifier
    classifier = MultinomialNB()
    classifier.fit(X_train_vect, y_train)

    # Save the trained model and vectorizer
    with open(model_path, 'wb') as f:
        pickle.dump(classifier, f)
    
    with open(vectorizer_path, 'wb') as f:
        pickle.dump(vectorizer, f)

    # Evaluate the model
    y_pred = classifier.predict(X_test_vect)
    print(f"Model Evaluation for {file_path}")
    print(classification_report(y_test, y_pred))
    print(f"Model and Vectorizer saved for {file_path}")

# Train models for SMS and Email
load_and_train('sms_spam_corrected.csv', 'sms_classifier_model.pkl', 'sms_vectorizer.pkl')
load_and_train('email_spam.csv', 'email_classifier_model.pkl', 'email_vectorizer.pkl')
