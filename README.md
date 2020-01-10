# pyGlassWare
Framework for developing python applications that use HTML/CSS/javascript as a cross-platform graphical user interface - similar to Electron but without a 700MB overhead.

# Folder Setup

**./install.py** \
Python script that installs and downloads dependencies.

**./app.py** \
Python main application that starts server, and connects flask-socketio to a python interface object.

**./interface.py** \
Python object interface whose methods are callable via. *emit* events from flask-socketio.

**./templates/** \
Folder containing HTML template files to be served by app.py.

**./public/js/** \
Folder containing javascript files for GUI page.

**./public/css/** \
Folder containing CSS for GUI page.

**./public/images/** \
Folder containing images for GUI page.

# Executing a pyGlassWare project

The executable prototype for this project is currently in development.






<!-- -->
