from flask import render_template
from flask import Flask
from flask import jsonify
from flask import render_template 
from flask import redirect
from flask import url_for 
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route("/index <valor>", methods=["GET","POST"])
def index(valor):
    a=0
    for n in range(0,valor):
        divisores=0
        for div in range(1,n+1):
            if n % div == 0:
                divisores += 1 
        if divisores == 2:
            a=a+1
            #print('Contagem: {} do número Primo: {}'.format(a,n))    	
    #print('\n')
    return render_template('index.html', primo = n)

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)