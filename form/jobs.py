from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = TextAreaField('Заголовок', validators=[DataRequired()])
    work_size = StringField("Объем работы")
    is_finished = BooleanField("Завершено?")
    collaborators = StringField("Коллабораторы (имена через запятую)")
    team_leader = StringField("Лидер команды (имя)")
    submit = SubmitField('Применить')
