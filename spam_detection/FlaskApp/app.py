from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        message = request.form['message']
        prediction = 'spam' if "free" in message.lower() else 'ham'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)




# cd FlaskApp
# python app.py
# Open your web browser and go to the following URL to see the app in action

# click on : http://127.0.0.1:5000
# There will be a "message" text box and a "Submit" button.
# Enter a message in the text box and click "Submit" to see the prediction.
# e.g. "Congratulations! You've won a lottery!" or "Hello, how are you?".Prediction: spam
# e.g., "Hello, how are you?" Prediction: ham
# The app will display whether the message is classified as "spam" or "ham".
