# -*- coding: utf8 -*-
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os

from TwitterSearch import *

# server side 
# Initialize and configure Flask and SocketIO
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'secret'  
Bootstrap(app)



# routing/mapping a url on website to a python function 
@app.route('/', methods=['GET', 'POST']) #root directory, home page of website, called a decorator
def index():
    return render_template("index.html")


@app.route('/showtweets', methods = ['POST','GET'])
def showtweets():
    if request.method == 'POST':
        username = request.form['username']
        tweets=[]
        try:
            tuo = TwitterUserOrder(username) # create a TwitterUserOrder

            # create TwitterSearch object 
            ts = TwitterSearch(
                    consumer_key = 'JPIQgfrt5gTI90PgC2DNoLf44',
                    consumer_secret = 'wt1ciclku2cftRrv1WrNY3sidoSbRQ3xSP74fKO1dafT1pVHzn',
                    access_token = '15718225-77FWg39DfjuZIMRv4aqfuiEd3tM9TbmBHIFenF2tQ',
                    access_token_secret = 'qx9uoD5yzsUWeBgzVqIzChO7rruAvNjhomKmqua9nsfpl'
                    )

            # start asking Twitter about the timeline
            for tweet in ts.search_tweets_iterable(tuo):
                username = tweet['user']['screen_name']
                tweets.append( '%s' % ( tweet['text'] ) )

        except TwitterSearchException as e: # catch all those ugly errors
            print(e)

    return render_template("showtweets.html", tweets= tweets, username=username)

if __name__ == "__main__": #only start web server if this file is called directly  
    try:
        port = int(os.environ.get('PORT', 5000)) 
        app.run(debug=True, host='0.0.0.0', port = port)
    except KeyboardInterrupt:
        pass