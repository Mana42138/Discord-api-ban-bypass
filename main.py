from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/post_data', methods=['POST'])
def post_data():
  webhook_url = request.args.get('webhook')

  data = request.get_json()
  requests.post(webhook_url, json=data)
  return jsonify({'message': 'Data received successfully'})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
