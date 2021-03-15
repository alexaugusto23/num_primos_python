from flask import render_template
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import url_for 
from flask import request
import os 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/nprimos", methods=["GET","POST"])
def primos():

    max_qts_primos_total = int(request.args.get("valor"))

    qtds_primo_encontrados = 1
    num_primos = [2]
    candidato_primo = 3

    while qtds_primo_encontrados < max_qts_primos_total:

        if (verifica_primo(candidato_primo)):
            num_primos.append(candidato_primo)
            qtds_primo_encontrados += 1
        candidato_primo += 1
    print(num_primos)

    return render_template('primos.html', tam = len(num_primos), lista = num_primos)

def verifica_primo(candidato_primo): 
        ehprimo = True
        for i in range(2, candidato_primo):
            if candidato_primo % i == 0:
                ehprimo = False
                break
        return ehprimo    


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='127.0.0.1', port=port)