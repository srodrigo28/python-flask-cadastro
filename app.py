from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'

@app.route('/submit', methods=['GET', "POST"])
def submit():
    if request.method == 'POST':
        data = request.form['nome']

        return f'Você enviou {data}'
    return '''
        <form method="POST">
            Nome: <input type="text" name="nome">
            <input type="submit" value="Enviar" />
        </form>
    '''

@app.route('/template')
def template():
    return render_template('index.html', name="Ana Júlia", age=28, male='feminino' ) 

# Roda aplicação
if __name__ == '__main__':
    app.run(debug=True, port=7070)