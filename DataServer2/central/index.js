//  Import data-types.json
const dataTypes = require('./data-types.json');

const db = require("./db");
const express = require('express');
const app = express();

// Enable CORS for all domains
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  next();
});


// Endpoint to get data types
app.get('/get-data-types', (req, res) => {
  res.send(dataTypes);
});

// Endpoint to get data points
app.post('/get-data-points', (req, res) => {
  console.log(req.body);
  const dataPoints = [
    {id: 1, name: 'Data Point 1', value: 100},
    {id: 2, name: 'Data Point 2', value: 200},
    {id: 3, name: 'Data Point 3', value: 300}
  ];
  res.send(dataPoints);
});

// Endpoint to get data
app.get('/get-data', (req, res) => {
  const data = {
    dataType: 'string',
    dataPoints: [
      {id: 1, name: 'Data Point 1', value: 'Hello'},
      {id: 2, name: 'Data Point 2', value: 'World'},
      {id: 3, name: 'Data Point 3', value: '!'}
    ]
  };
  res.send(data);
});

// Listen on port 3000
app.listen(3000, () => {
  console.log('Server listening on port 3000...');
});
