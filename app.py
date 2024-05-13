from flask import Flask, request, jsonify
# import seu_script_python

app = Flask(__name__)

@app.route('/processar-imagem', methods=['POST'])
def processar_imagem():
    if 'imagem' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    imagem = request.files['imagem']

    # Salve a imagem em um diretório temporário ou onde preferir
    imagem.save('caminho/para/salvar/imagem.jpg')

    # Chame seu script Python para processar a imagem
    resultado = seu_script_python.processar_imagem('caminho/para/salvar/imagem.jpg')

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
