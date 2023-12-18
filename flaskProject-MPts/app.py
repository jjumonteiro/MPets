from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'Mundo Pets'

@app.route('/')
def home():
    return render_template('home.html', Titulo = "Mundo pets")

# Essa rota puxa o HTML Home com todas as suas informações, para que na pagina possa aparecer a pagina inicial.
# Após o app.route podemos observar uma / onde ela nos o acesso dela no site, assim quando clicar na guia INICIO
# ira entrar na pag home.

# No return colocamos o documento que sera preciso para fazer a alteração na ropta e o titulo após é para aparecer na guia do site.

@app.route('/produtos')
def produtos():
    return render_template('prodt.html', Titulo = "Mundo pets")

@app.route('/dicas')
def dicas():
    return render_template('dicas.html', Titulo = "Mundo pets")

if __name__ == '__main__':
    app.run()
