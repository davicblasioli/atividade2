from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', maior='', menor='', media='')

@app.route('/resultado', methods=['POST'])
def resultado():
    maio = float('-inf')  # Define o maior valor como negativo infinito
    meno = float('inf')   # Define o menor valor como infinito
    soma = 0
    qntd = 0

    for qntd in range(10):
        numero = int(request.form['numero' + str(qntd)])
        if numero > maio:
            maio = numero
        if numero < meno:
            meno = numero
        soma += numero
        qntd += 1

    media = soma / qntd
    return render_template('index.html', maio=maio, meno=meno, media=media)

if __name__ == '__main__':
    app.run(debug=True)
