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

    def on_timertest(self, data):
        print("starting timer test");
        # validate arguments ----------------------------------------
        try: iterations = int(data['iterations']);
        except:
            emit('console', {
                'command': 'log',
                'arg': 'Invalid value for iterations argument',
            });
        try: delay = float(data['delay']);
        except:
            emit('console', {
                'command': 'log',
                'arg': 'Invalid value for delay argument',
            });
        # -----------------------------------------------------------
        emit('console', {
            'command': 'log',
            'arg': (
                "Beginning timer test, delay "+str(delay)+"s, "+
                str(iterations)+" iterations."
            )
        });
        for i in range(0, iterations):
            emit('console', {
                'command': 'log',
                'arg': str(i)
            });
            print(i);
            eventlet.sleep(delay);
