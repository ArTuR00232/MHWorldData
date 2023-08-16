import sys
sys.path.append('./app/front/')
#flask to api, front react and electron to .exe
from flask import Flask, render_template


app = Flask(__name__, template_folder = '../front')



@app.route('/')
def home():
    #return 'oi'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)