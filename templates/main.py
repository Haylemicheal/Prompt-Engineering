from flask import Flask, render_template
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html')

if __name__ == '__main__':
   app.run(debug = True)