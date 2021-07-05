from flask import Flask, jsonify, request
from lib import functions as func
import lib.words as words

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Assitante vocal page d'accueil<h2/>"

@app.route('/assistant_logiciel/api/translate_text_to_hasaniya', methods=['POST'])
def reception_envoie():
    content = request.get_json(force=True)
    return jsonify({'result': func.hsaniya_google_to_hasniya_general(content['text'], words=words.words)})


if __name__ == '__main__':
    app.run()