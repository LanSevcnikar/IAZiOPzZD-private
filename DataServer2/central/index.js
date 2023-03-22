const fetch = require("node-fetch");
//  Import data-types.json

const dataTypes = require("./data-types.json");

const db = require("./db");
const express = require("express");
var bodyParser = require("body-parser");
const app = express();

app.use(bodyParser.json());

// Enable CORS for all domains
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  next();
});

// define a function that given two lat and two lng coordinates calculates the distance in km
function distanceLatLng(lat1, lon1, lat2, lon2) {
  var p = 0.017453292519943295; // Math.PI / 180
  var c = Math.cos;
  var a =
    0.5 -
    c((lat2 - lat1) * p) / 2 +
    (c(lat1 * p) * c(lat2 * p) * (1 - c((lon2 - lon1) * p))) / 2;

  return 12742 * Math.asin(Math.sqrt(a)); // 2 * R; R = 6371 km
}

// Endpoint to get data types
app.get("/get-data-types", (req, res) => {
  res.send(dataTypes);
});

// Endpoint to get data points
app.post("/get-data-points", (req, res) => {
  console.log(req.body);
  let dataPoints = [];
  let lat = req.body.location.lat;
  let lng = req.body.location.lng;
  let rad = req.body.location.rad;

  for (let i = 0; i < req.body.dataTypes.length; i++) {
    let dataType = req.body.dataTypes[i];
    let dataTypeName = dataType.dataTypeName;
    let dataPoint = db.dataPoints.list().filter((dp) => {
      let distance = distanceLatLng(lat, lng, dp.lat, dp.lon);
      return dp.dataType === dataTypeName && distance <= rad;
    });
    dataPoints.push(...dataPoint);
  }

  console.log(dataPoints);

  res.send(dataPoints);
});

// Endpoint to get data
app.post("/get-data", (req, res) => {
  console.log(req.body);
  let data = [
    {
      id: "HkF-BpZmf1n",
      ARSO_id: "1828",
      dataPointName: "LJUBLJANA - BEŽIGRAD",
      lat: 46.06550561584517,
      dataType: "ARSO - povprečen zračni tlak (hPa)",
      ARSO_type_id: 12,
      lng: 14.51235900171941,
    },
  ];
  // make a request to the localhost:3001 server for each data point
  // and get the data

  // for each data point
  //   make a request to the localhost:3001 server
  //   get the data
  //   add the data to the data array

  for (let i = 0; i < data.length; i++) {
    let dataPoint = data[i];
    if (dataPoint.dataType.includes("ARSO")) {
      let url = "http://localhost:3001";
      let body = {
        ...dataPoint,
        startingDate: req.body.startingDate,
        endingDate: req.body.endingDate,
      };
      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      })
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data);
          res.send(data);
        });
    }
  }
});

// Listen on port 3000
app.listen(3000, () => {
  console.log("Server listening on port 3000...");
});

metadata_request = {
	start_date: "yyyy-mm-dd",
	end_date: "yyyy-mm-dd",
	location: {
		lat: xxxxx,
		lon: xxxxx,
	},
	radius: x,
}