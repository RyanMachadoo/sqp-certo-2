from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String())
  password = db.Column(db.String())
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.String())
    image = db.Column(db.String())
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.String())
    updated_at = db.Column(db.String())

todos = [ 
    {'title': 'João da Silva'},
    {'title':'Maria Souza'}
]

@app.route('/')
def index():
  return render_template(
      'index.html',
      todos = todos
  )

@app.route('/contats', methods=['POST'])
def contats():
    title = request.form.get('title')
    todos.append({'title':title})
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=8080)