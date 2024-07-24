from flask import Flask, logging, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route("/")
def test():
  return "<h1> Live Test </h1><p>Server is active</p>"

@cross_origin()
@app.route('/submit/image', methods=['POST'])
def submit_image():
  image = request.files['image']
  image.save('./image.jpg')
  image.save(f'assets/images/{secure_filename(image.filename)}')
  cmd = ['python', 'scripts/image.py']
  output = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
  print(output)
  response = jsonify({"result": output.__str__()})
  return response

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)