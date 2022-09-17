from flask import Flask, render_template, request
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from scripts.news_classifier_pipline import Pipeline

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/news')
def news():
   return render_template('news.html')

@app.route('/bnewscore')
def newsscore():
   title = request.args.get('title')
   desc = request.args.get('desc')
   pipe = Pipeline()
   pred = pipe.pipeline(title, desc)
   return render_template('news.html', prediction=pred)

@app.route('/jdentities')
def job_desc_entities():
   return render_template('job_desc_ent.html')


if __name__ == '__main__':
   app.run(debug = True)