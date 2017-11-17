from flask import Flask
from config import DevConfig

app = Flask(_name_)
app.config.from_object(DevConfig)

@app.route('/')
def home():
        return '<h1>Hello World!</h1>'

    if _name_ == '_main_': 
        app.run()
