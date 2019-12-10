import os, sys;
import numpy as np, pandas as pd;
import eventlet;
from flask_socketio import Namespace, emit;
################################################################################
class interface(Namespace):
    def __init__(self, *args, **kwargs):
        super(interface, self).__init__(*args, **kwargs);
        self.templateVars = { };
        self.active = False;
        self.killswitch = False;
        self.seqs = pd.DataFrame();

    def on_connect(self):
        print("socket connected");

    def on_disconnect(self):
        print("socket disconnected");

    def on_say(self, data):
        print("SAY:");
        print("------------------------");
        print(data);
        print("------------------------");

    def on_control(self, command):
        print("got to control");
        if command=="begin":
            print("Beginning.");
            self.active = True;
            emit('console',{
                'command':'log',
                'arg': 'python beginning'
            });

    def on_throughlog(self, message):
        print("got throughlog, bouncing back");
        emit('console',{
            'command': 'log',
            'arg': message,
        });

    def on_kill(self, message):
        print("GOT KILL");
        self.killswitch = True;
