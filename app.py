from flask import Flask, render_template

app = Flask(__name__)

# Главная страница (localhost:5000/)
@app.route('/')
def index():
    return render_template('main.html')

# Ваш старый маршрут, который вы прописали в HTML
@app.route('/about-us')
def page1():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)