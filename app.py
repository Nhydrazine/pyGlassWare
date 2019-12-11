import sys, os;
from flask import Flask, render_template, request, send_from_directory;
from flask_socketio import SocketIO, Namespace, emit;
from interface import interface;
# initialize flask ------------------------------------------------------------#
app = Flask(__name__);
app.config['SECRET_KEY'] = "secret";
socketio = SocketIO(app);
# load interface --------------------------------------------------------------#
appInterface = interface('/');
# root ------------------------------------------------------------------------#
@app.route('/')
def hello_world():
    return render_template('indexd3.html', **appInterface.templateVars);
# static file paths (js/css) --------------------------------------------------#
@app.route('/public/<path:path>')
def send_static(path):
    return send_from_directory('public', path);
# socket events ---------------------------------------------------------------#
socketio.on_namespace(appInterface);
# run -------------------------------------------------------------------------#
socketio.run(app);
#------------------------------------------------------------------------------#
