#!/usr/bin/python3
"""Display list of State objects"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def display_states():
    states = storage.all('State')
    return render_template('9-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
