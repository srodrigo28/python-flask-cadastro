from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Olá, mundo!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('name')
        senha = request.form.get('senha')
        return f'Login recebido: {email}', senha
    
    return '''
    <form method="POST">
        E-mail: <input type="text" name="name"><br>
        Senha:  <input type="password" name="senha"><br><br>
        
        <button type="submit">Entrar</button>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=7070)