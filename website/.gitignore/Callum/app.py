from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# new instance of the Flask class
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300), unique=True)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=['POST'])
def add():
    task = request.form.get('task')
    new_todo = Todo(task=task)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)