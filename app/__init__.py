from flask import Flask

app = Flask(__name__)
app.debug = False

from app import views
