# SMS-and-EMAIL-Spam-Detection

Step 1: Set Up Your Environment
Install Python and Required Libraries: First, ensure that Python (preferably 3.7 or higher) is installed on your system. Then, create a virtual environment and install the necessary dependencies.

bash
Copy code
# Create a virtual environment
python -m venv spam_detection_env

# Activate the virtual environment
# On Windows
spam_detection_env\Scripts\activate
# On macOS/Linux
source spam_detection_env/bin/activate

# Install required libraries
pip install flask pandas scikit-learn numpy
Download or Create the Dataset: The code assumes that you have two datasets:

sms_spam_corrected.csv: SMS spam data (label: "Label", message: "Message").
email_spam.csv: Email spam data (label: "Label", message: "Message").
Make sure your CSV files are available in the same directory as your script or provide the correct path to the load_and_train function.

Prepare the Models: The load_and_train function in your code trains models for both SMS and email spam detection using Naive Bayes. You need to run the training script (Python file) first to generate the model files (sms_classifier_model.pkl, email_classifier_model.pkl, sms_vectorizer.pkl, and email_vectorizer.pkl).

Run the training script: Save the first block of code (the one with model training) as train_models.py and execute it to generate the required pickle files.

bash
Copy code
python train_models.py
After running this script, you will have the following files:

sms_classifier_model.pkl: Trained SMS spam detection model.
email_classifier_model.pkl: Trained email spam detection model.
sms_vectorizer.pkl: Vectorizer used for SMS data.
email_vectorizer.pkl: Vectorizer used for email data.
Prepare Flask Application: The Flask app will serve as the web interface for interacting with the spam detection models. Save the second block of code (the Flask app) as app.py.

Ensure that the model and vectorizer pickle files are in the same directory as app.py, or modify the paths accordingly in the app.

Prepare HTML Template: The HTML file index.html is the frontend where users can input SMS or email messages for spam detection.

Save the provided HTML code in the templates folder inside your project directory:

Create a folder named templates.
Save the HTML code as index.html inside the templates folder.
Folder structure:

markdown
Copy code
spam_detection_project/
├── app.py
├── train_models.py
├── sms_spam_corrected.csv
├── email_spam.csv
├── sms_classifier_model.pkl
├── email_classifier_model.pkl
├── sms_vectorizer.pkl
├── email_vectorizer.pkl
└── templates/
    └── index.html
Step 2: Run the Flask Application
Start the Flask app: Once everything is set up, you can run the Flask application to start the web server.

bash
Copy code
python app.py
Access the Web Interface: After running the Flask app, you should be able to access the application in your browser. By default, Flask runs on localhost (or 127.0.0.1) and port 5000.

Open your browser and go to:

arduino
Copy code
http://127.0.0.1:5000/
The web page will display two forms: one for SMS spam detection and one for email spam detection.

Test the Spam Detection:

Enter a message in the SMS or email input field.
Click "Check SMS" or "Check Email".
The result (either "Spam" or "Not Spam") will be displayed below the form.
Step 3: Deploy the Application (Optional)
If you'd like to deploy this web application to a cloud platform like Heroku or AWS, follow the respective deployment instructions for Flask applications.

For Heroku:
Install the Heroku CLI and set up a Heroku app.
Create a Procfile in the root directory with the following content:
makefile
Copy code
web: python app.py
Initialize a Git repository, commit your code, and push it to Heroku:
bash
Copy code
git init
git add .
git commit -m "Initial commit"
heroku create
git push heroku master
Open your app in a browser:
bash
Copy code
heroku open
Summary of Steps:
Install dependencies.
Train the models using the provided script.
Run the Flask app to serve the web interface.
Access the app and test the SMS and email spam detection functionality.
