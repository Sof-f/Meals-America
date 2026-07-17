from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/about')
def about_page1():
    return render_template('about.html')

@app.route('/how')
def how_page():
    return render_template('how.html')

if __name__ == '__main__':
    app.run(debug=True)