from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

@app.route('/')
def index():
    current_date = datetime.now().strftime("%B %d, %Y")
    return render_template('index.html', current_date=current_date)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')

if __name__ == '__main__':
    app.run(debug=True)


