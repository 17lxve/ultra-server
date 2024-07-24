from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
# @cross_origin
def test():
  return "<h1> Live Test </h1><p>Server is active</p>"

@app.route('/submit/image', methods=['POST'])
# @cross_origin
def submit_image():
  image = request.files['image']
  image.save('./image.jpg')
  image.save(f'assets/images/{secure_filename(image.filename)}')
  cmd = ['python', 'scripts/image.py']
  output = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
  print(output)
  return "{result:" + f"{output}" +"}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)