from flask import Flask #import flask class object from flask library

app = Flask(__name__) #instantiating the flask object #__name__ gets the name of the python script

@app.route('/sd-script/') #decorator - url name extender
def home():
    return "Website content goes here!"

if __name__=="__main__":
    app.run(debug = True)