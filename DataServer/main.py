from flask import Flask, jsonify
import requests

from sensor_community.sc_get_locations import get_sensor_community_locations

app = Flask(__name__)

@app.route('/sensor.community')
def get_sensor_community_data():
    response = get_sensor_community_data()
    print(response)

@app.route('/ARSO')
def get_arso_data():
    response = requests.get('http://www.arso.gov.si/xml/vreme/napovedi/v2.0/json/')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
