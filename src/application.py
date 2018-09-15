from flask import *
from datetime import datetime
from modules.mod_staticdata import StaticData
from modules.mod_requestor import Requestor
app = Flask(__name__)

@app.route('/')
def index():
    currentdate = datetime.now().strftime('%Y-%m-%d')
    # Static data for testing purposes
    # req = StaticData()
    # neo_data_json = json.loads(req.get_neodata(currentdate))
    # objlist = neo_data_json['near_earth_objects']['2018-09-13']

    # Get data from NEO API
    req = Requestor()
    neo_data_json = json.loads(req.get_neodata(currentdate))
    objlist = neo_data_json['near_earth_objects'][currentdate]

    return render_template('index.html', objlist=objlist, currentdate=currentdate, rawoutput=neo_data_json)

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)



