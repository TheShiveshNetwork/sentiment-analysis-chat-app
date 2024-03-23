import nltk
from flask import request, Flask, render_template


app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')

messages = []


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text))))['compound']
    if(score > 0):
        label = 'positive'
    elif(score == 0):
        label = 'neutral'
    else:
        label = 'negative'
    messages.append({'msg': text, 'score': label})
    return(render_template('index.html', messages=messages))


if __name__ == "__main__":
    app.run(port='8088', threaded=False, debug=True)