from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# instalado: python -m pip install flask_wtf
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'

class RegisterForm(FlaskForm):
    first_name = StringField('Primeiro nome')
    last_name  = StringField('Sobrenome')
    email      = StringField('E-mail')
    password   = PasswordField('Senha')
    confirm    = PasswordField('Confirme a senha')
    
    submit     = SubmitField('Cadastrar')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

# Roda aplicação
if __name__ == '__main__':
    app.run(debug=True, port=7070)
