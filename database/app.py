import flask
import pymongo
from flask import Flask,request
from pymongo import MongoClient
from flask_table import Table,Col

# Web Table
class PositionTable(Table):
    portfolio = Col('Portfolio')
    position = Col('Position')
    market_value = Col('Market Value')

    allow_sort = True
    def sort_url(self,col_key,reverse=False):
        if reverse:
            direction = 'desc'
        else:
            direction = 'asc'
        return flask.url_for('index',sort=col_key,direction=direction)

class Position(object):
    def __init__(self,portfolio,position,market_value):
        self.portfolio=portfolio
        self.position=position
        self.market_value=market_value

# DB query function
def getTable(sort_key="_id",sort_dir="asc",gt=None):
    client = MongoClient()
    
    positions=[]
    
    if sort_key == "portfolio":
        sort_key="_id"

    if sort_dir == "desc":
        sort=-1
    else:
        sort=1
    # This query performs necessary aggregation and multiplicaiton to yield position and market value per portfolio
    if gt and gt != "":
        res = client.kls.securities.aggregate([{"$unwind":"$trades"},{"$group":{"_id":"$trades.portfolio","position":{"$sum":"$trades.trade"},"price":{"$first":"$price"},"multiplier":{"$first":"$multiplier"}}},{"$project":{"_id":1,"position":1,"market_value":{"$multiply":["$position","$price","$multiplier"]}}},{"$match":{"market_value":{"$gt": int(gt)}}},{"$sort":{sort_key:sort}}])
    else:
        res = client.kls.securities.aggregate([{"$unwind":"$trades"},{"$group":{"_id":"$trades.portfolio","position":{"$sum":"$trades.trade"},"price":{"$first":"$price"},"multiplier":{"$first":"$multiplier"}}},{"$project":{"_id":1,"position":1,"market_value":{"$multiply":["$position","$price","$multiplier"]}}},{"$sort":{sort_key:sort}}])
    for doc in res:
        positions.append(Position(doc['_id'],doc["position"],doc["market_value"]))
    return PositionTable(positions).__html__()

# Form

def getPreservedForm(args):
    value = ""
    if "gt" in args:
        value = args["gt"]
    form = 'Market Value Greater Than: <form method="get"><input name="gt" value="%s"></input>' % value
    for key,value in args.iteritems():
        form += '<input type="hidden" name="%s" value="%s" />' % (key,value)
    form += '<button type="submit">Go!</button></form>'
    return form
    

# Flask App
app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    gt=""
    if "gt" in request.args and request.args.get("gt").isdigit():
        gt = request.args.get("gt")
    if "sort" in request.args and "direction" in request.args:
        return getPreservedForm(request.args) +  getTable(sort_key=request.args.get('sort'),sort_dir=request.args.get('direction'),gt=gt)
    return getPreservedForm(request.args) +  getTable(gt=gt)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

