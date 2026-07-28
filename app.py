from flask import Flask, render_template, redirect, url_for  # Добавили redirect и url_for
from forms import LoginForm  
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
app.config['SECRET_KEY'] = 'your_secret_key'  # Оставили один секретный ключ

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(150), nullable=True) # Опционально
    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=True)        # Опционально
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    about = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.Text, nullable=True)             # Опционально


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/about')
def about_page1():
    return render_template('about.html')

@app.route('/how')
def how_page():
    return render_template('how.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html')

@app.route('/get-started', methods=['GET', 'POST'])
def get_sterted():
    form = LoginForm()
    
    if form.validate_on_submit():
        print("\n" + "="*40)
        print("Data from forms:")
        print(f"Name:         {form.Name.data}")
        print(f"Organise: {form.Organization.data}")
        print(f"Phone:     {form.Phone.data}")
        print(f"Email:       {form.Email.data}")
        print(f"City:       {form.City.data}")
        print(f"State: {form.State.data}")
        print(f"Country: {form.Country.data}") # Добавили в принты вашу страну
        print(f"Zip-код:     {form.Zip.data}")
        print(f"Who:{form.About.data}")
        print(f"Comment: {form.Comment.data}")
        
        # ========================================================
        # 2. ДОБАВИЛИ СОХРАНЕНИЕ ДАННЫХ В ТАБЛИЦУ
        # ========================================================
        new_order = Order(
            name=form.Name.data,
            organization=form.Organization.data,
            phone=form.Phone.data,
            email=form.Email.data,
            city=form.City.data,
            state=form.State.data,
            country=form.Country.data,  # Сохраняем поле страны
            zip_code=form.Zip.data,
            about=form.About.data,
            comment=form.Comment.data
        )
        db.session.add(new_order)
        db.session.commit() # Физически записываем в site.db
        print("Successfully saved to database!")
        print("="*40 + "\n")
        
        # Перенаправляем пользователя на страницу Спасибо
        return redirect(url_for('thank_you'))

        
    else:
        if form.errors: # Печатаем ошибки только если они реально есть при POST-запросе
            print("Something gone wrong:", form.errors)
  
    return render_template('get__started.html', form=form)

@app.route('/thank-you')
def thank_you():
    return "<h1>Thank you! Your application has been successfully submitted and saved.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
