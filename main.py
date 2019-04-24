# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import render_template
from flask import abort
from jinja2 import exceptions

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

# Support both with and without trailing slash.
@app.route('/<page>/')
@app.route('/<page>')
def template_page(page):
  try:
    return render_template('{}.html'.format(page.strip('/')))
  except exceptions.TemplateNotFound as e:
    return abort(404)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
