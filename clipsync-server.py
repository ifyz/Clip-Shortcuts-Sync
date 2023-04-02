from flask import Flask, request, jsonify
import json

app = Flask(__name__)
clipboard_data = {
    "ios": "",
    "windows": ""
}

@app.route('/clipboard', methods=['POST'])
def set_clipboard():
    platform = request.form.get('platform')
    content = request.form.get('content')
    clipboard_data[platform] = content
    return jsonify({"status": "success"})

@app.route('/clipboard', methods=['GET'])
def get_clipboard():
    platform = request.args.get('platform')
    content = clipboard_data.get(platform, "")
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=8000)
