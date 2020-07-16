from bottle import route,run
import bottle
from joblib import load
from get_tweets import get_related_tweets
import pandas as pd
import simplejson as json


pipeline = load("text_classification.joblib")
pd.set_option("display.max_rows", None, "display.max_columns", None)


def requestResults(name):
    tweets = get_related_tweets(name)
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
    data = str(tweets.prediction.value_counts()) + '\n\n'
    return data + str(tweets)


app= bottle.Bottle()

bottle.TEMPLATE_PATH.insert(0,"./")

@route('/', method=['POST', 'GET'])
def hello():
    if bottle.request.method == 'POST':
        user = str(bottle.request.body.read().decode("utf-8"))
        user = user.split("=")
        return bottle.redirect('/success/'+user[1])
    else:
        return bottle.template("./templates/home.html")

@route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "

run(host='localhost', port=5000, debug=True)
"""
@app.route('/',methods=["GET"])
def home():
    return "Hello World!"


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if bottle.request.method == 'POST':
        user = bottle.request.body.read()
        return bottle.redirect('/success/{{name}}', name=user)


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


run(app,reloader=True,port =3000)
"""
