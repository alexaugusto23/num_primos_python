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

@app.route("/primos", methods=["GET","POST"])
def primos():
    total = request.args.get("valor")
    qts_primos_tot = int(total)
    
    qtds_primo = 1
    num_primos = [2]
    numero = 3

    while qtds_primo  < qts_primos_tot:
        ehprimo = True
        for i in range(2, numero):
            if numero % i == 0:
                ehprimo = False
                break
        if (ehprimo):
            num_primos.append(numero)
            qtds_primo += 1
        numero += 1
    print(num_primos)

    return render_template('primos.html', tam = len(num_primos), lista = num_primos)

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='127.0.0.1', port=port)