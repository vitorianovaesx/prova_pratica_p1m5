from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

data = []

#Rota pra pegar 
@app.route('/pegar', methods=['GET'])
def pegar():
   return jsonify({'data': data})

#Rota pra enviar
@app.route('/enviar', methods=['POST'])
def enviar():
   record = request.json
   record['data'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   data.append(record)
   return jsonify({'mensagem': 'Adicionado com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
