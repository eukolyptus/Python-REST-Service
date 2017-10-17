#######################################################
#####
##### Assignment 1
##### You will be implementing a dynamic Python invoker REST service. The service will have the following features:
#####   [1] Python Script Uploader
#####   [2] Python Script Invoker
##### URL: https://github.com/sithu/cmpe273-fall17/tree/master/assignment1#request-1
##### Resources used:
#####   [1] https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#####   [2] http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
#####
#######################################################

import os
from flask import Flask, request, abort, jsonify, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'py'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# scripts json array take two attributes; script_id and script_run
scripts = [
    {
        'script_id': 1,
        'script_run': u'print("This is script id 1")'
    }
]


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/v1/scripts', methods=['POST'])
def create_task():
    # POST
    if request.method == 'POST':
        # check if the post request has the file part
        if 'data' not in request.files:
            print('No file part')
            return ""
        file = request.files['data']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return ""
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # PARSE foo.py
            sample = open(filename, 'r')
            sample.readline()  # first line (i.e.: name of file)
            result = sample.readline()

            script = {
                'script_id': scripts[-1]['script_id'] + 1,
                'script_run': result
            }
            scripts.append(script)
            return ""


@app.route('/api/v1/scripts/<int:script_id>', methods=['GET'])
def get_task(script_id):
    script = [script for script in scripts if script['script_id'] == script_id]
    if len(script) == 0:
        abort(404)

    return "", exec(script[0]['script_run'])


@app.route('/')
def index():
    return "CMPE283 Assignment 1\n"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
