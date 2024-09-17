from flask import Flask

app = Flask(__name__)

from app import routes  # Make sure routes are imported after the app is initialized
