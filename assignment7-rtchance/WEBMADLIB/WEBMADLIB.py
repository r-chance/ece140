# WEBMADLIB/WEBMADLIB.py

import os
from flask import Flask, render_template, g, request, redirect
from sqlite3 import dbapi2 as sqlite3
from flask import jsonify
##### APP SETUP #####
app = Flask(__name__)

##### DB SETUP #####

# Setup the database credentials
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'WEBMADLIB.db'),
    DEBUG=True,
    #SECRET_KEY=b'<SOME HEXADECIMAL SECRET KEY>',
    USERNAME='admin',
    PASSWORD='pass'
))

# Connect to the DB
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Wrap the helper function so we only open the DB once
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Create the database (we do this via command line!!!)
def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# Command to create the database via command line
# You call it from command line: flask initdb
@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

# Close the database when the request ends
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

##### ROUTES #####

@app.route('/')
def GET_companies() :
    db = get_db()
    cur = db.execute('SELECT * from businesses')
    the_businesses = cur.fetchall()
    if (len(the_businesses) == 0):
        raise AssertionError;
    return render_template('madlib.html', entries=the_businesses)



@app.route('/horsemen/<name>', methods=["GET"])
def get_route(name):
    db = get_db()
    cur = db.execute("SELECT * from businesses where business_name = ?",(name,))
    the_business = cur.fetchall()
    return jsonify(id = the_business[0][0],
                   business_name=the_business[0][1],
                business_type=the_business[0][2],
                market_type=the_business[0][3],
                job_to_be_done=the_business[0][4],
                revenue_model=the_business[0][5])
