#from wsgiref.validate import validator
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLAlCHEMY_DATABASE_URI'] = "sqlite:///databse.db"
app.config['SECRET_KEY'] = 'f8475b1763454e3ba94a25b809cf8193'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50), nullable=False)

class TodoForm(FlaskForm):
    todo = StringField('Enter Todo', validators=[InputRequired(), Length(min=4, max=50)])
    submit = SubmitField('Add Todo')

@app.route('/')
def home():
    form = TodoForm()
    return render_template('home.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)