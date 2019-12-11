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

    def on_pandastest(self, data):
        df = pd.DataFrame({
            'col1': np.random.randint(0,100,50),
            'col2': np.random.randint(0,100,50),
            'col3': np.random.randint(0,100,50),
            'col4': np.random.randint(0,100,50),
            'col5': np.random.randint(0,100,50),
            'col6': np.random.randint(0,100,50),
            'col7': np.random.randint(0,100,50),
            'col8': np.random.randint(0,100,50),
        });
        emit('console', {
            'command': 'log',
            'arg': df.to_string().replace("\n","<br>")
        });

    def on_numpyhistotest(self, data):
        emit('console', {
            'command': 'log',
            'arg': "Histogram test: 1000 random numbers"
        });
        nums = np.random.random(1000);
        hist, bins = np.histogram(nums, bins=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]);
        display = [];
        for i in range(0, len(hist)):
                display.append(
                    str(bins[i])+"-"+str(bins[i+1])+
                    ": "+str(hist[i])
                );
        emit('console', {
            'command': 'log',
            'arg': "\n".join(display)
        });
