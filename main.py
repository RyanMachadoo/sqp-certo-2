from flask import Flask, render_template, request, redirect
app = Flask('app')

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
    app.run(host='0.0.0.0', port=8080)