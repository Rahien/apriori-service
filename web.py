import flask
import json
from database import fetch_transactions, transaction_iterator, transaction_count
from apriori import apriori
import thread
import sys
import os
import helpers
import pdb
from multiprocessing import Manager

sys.setrecursionlimit(10000)

processes = {}

@app.route("/version")
def version():
    return "frequent-items v.0.0.1"

@app.route("/transactions/<config>")
def transactions(config):
    return flask.jsonify(fetch_transactions(config))

@app.route("/apriori/<config>")
def do_apriori(config):
    id = helpers.generate_uuid()

    result = apriori(config)

    return flask.Response(response = json.dumps(result) , status=200, mimetype="application/json")
