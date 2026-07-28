from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional 


class LoginForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    Organization = StringField('Organization', validators=[Optional()])
    Phone = StringField('Phone Number', validators=[DataRequired()])
    Email = StringField('E-mail Address', validators=[Optional()])
    City = StringField('City', validators=[DataRequired()])
    State = StringField('State', validators=[DataRequired()])
    Country = StringField('Conutry', validators=[DataRequired()])
    Zip = StringField('Zip Code', validators=[DataRequired()])
    About = SelectField('Tell us about your needs ', validators=[DataRequired()], choices=[
        (' ', '—Please choose an option—'),
        ('customer',"I'm a current customer needing assistance"),
        ('caregiver', "I'm a caregiver or need meals for myself"),
        ('manager', "I'm a case manager needing meals for clients"),
        ('organisation', "I represent a healthcare organization needing information for patients")

    ])
    Comment = TextAreaField('Additional Comments', validators=[Length(max=1000)])
    Submit = SubmitField('Submit')
