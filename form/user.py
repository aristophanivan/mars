from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя космонавта', validators=[DataRequired()])
    surname = StringField('Фамилия космонавта', validators=[DataRequired()])
    age = StringField('Возраст космонавта', validators=[DataRequired()])
    position = StringField('Позиция космонавта', validators=[DataRequired()])
    speciality = StringField('Cпециализация космонавта', validators=[DataRequired()])
    address = StringField('Адрес космонавта', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
