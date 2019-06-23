from flask import Flask, request, jsonify
from flask_cors import CORS
from config import FLAG, HASH

app = Flask(__name__)
CORS(app)


@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    text = data['text']
    isMatched = check_hash(text)

    if isMatched:
        text = 'Hash value is matched! Flag is {0}'.format(FLAG)
    else:
        text = 'Hash value is unmatched. Keep trying!'

    return jsonify(content=text)


def check_hash(text):
    hash = 0
    text_list = list(text)

    for i in range(len(text_list)):
        ord_char = ord(text_list[i])
        hash += int(ord_char)

    if hash == int(HASH):
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
