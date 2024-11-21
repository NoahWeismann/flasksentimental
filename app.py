from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def sentimentanalysis():
    
    sentiment = ''
    input_text1 = ''
    if request.method=='POST' and 'input_text' in request.form:
        input_text1 = request.form.get('input_text')
        blob = TextBlob(input_text1)
        sentiment = blob.sentiment.polarity #-1 to 1
    return render_template('home.html', sentiment = sentiment, input_text1 = input_text1)
