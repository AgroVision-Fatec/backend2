from flask import Flask, request, jsonify
import os
from contabilizar_pragas import script_pragas



app = Flask(__name__)

@app.route('/processar-imagem', methods=['POST'])
def processar_imagem():
    if 'imagem' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    imagem = request.files['imagem']
    imagem.save('IA/imgs/imagem.jpg')

    resultado = script_pragas()
  

    os.remove('IA/imgs/imagem.jpg')
    return jsonify({'resultado': resultado})


@app.route('/', methods=['GET'])
def home():
    return jsonify({'mensagem': 'Aplicativo Flask rodando'})


if __name__ == '__main__':
    app.run(debug=True)
