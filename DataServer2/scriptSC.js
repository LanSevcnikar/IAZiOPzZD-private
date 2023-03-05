let all_sensors = require("./../Testing/sensor.community/device-scrape/GUI/data/sensors.json");

// create a dictionary / map where I will count how many types of each sensor there are
let sensor_types = {};

// filter out all sensors that dont have long between 10 and 20 and lat between 43 and 47
all_sensors = all_sensors.filter(
  (sensor) =>
    sensor.location.longitude > 10 &&
    sensor.location.longitude < 20 &&
    sensor.location.latitude > 43 &&
    sensor.location.latitude < 47
);


// iterate through all sensors
for (let i = 0; i < all_sensors.length; i++) {
  // get the current sensor
  let sensor = all_sensors[i];

  // get the sensor type
  let sensor_type = sensor.sensor.sensor_type.name;

  // if the sensor type is not in the dictionary, add it
  if (!(sensor_types)) {
    sensor_types[sensor_type] = 0;
  }

  // increment the count of the sensor type
  sensor_types[sensor_type]++;
}

console.log(all_sensors.length);

// print the dictionary
console.log(sensor_types);

let humiditiy_sensors = [
  "BME280",
  "DHT22",
  "SCD30",
  "SHT11",
  "SHT15",
  "SHT30",
  "SHT31",
  "SHT35",
  "SHT85",
]

let temperature_sensors = [
  "BME280",
  "BMP180",
  "DHT22",
  "SCD30",
  "SHT11",
  "SHT15",
  "SHT30",
  "SHT31",
  "SHT35",
  "SHT85",
]

let PM10_sensors = [
  "PMS1003",
  "PMS3003",
  "PMS5003",
  "PMS7003",
  "SDS011",
]

let PM25_sensors = [
  "PMS1003",
  "PMS3003",
  "PMS5003",
  "PMS7003",
  "SDS011",
]

const db = require("./central/db");


// iterate through all sensors
for (let i = 0; i < all_sensors.length; i++) {
  // get the current sensor
  let sensor = all_sensors[i];

  // get the sensor type
  let sensor_type = sensor.sensor.sensor_type.name;
  console.log(sensor_type);

  if(humiditiy_sensors.includes(sensor_type)) {
    db.dataPoints.create({
      SC_id: sensor.sensor.id,
      dataPointName: sensor.sensor.id,
      lon: sensor.location.longitude,
      lat: sensor.location.latitude,
      dataType: "sensor.community - humidity"
    })
  }

  if(temperature_sensors.includes(sensor_type)) {
    db.dataPoints.create({
      SC_id: sensor.sensor.id,
      dataPointName: sensor.sensor.id,
      lon: sensor.location.longitude,
      lat: sensor.location.latitude,
      dataType: "sensor.community - temperature"
    })
  }

  if(PM10_sensors.includes(sensor_type)) {
    db.dataPoints.create({
      SC_id: sensor.sensor.id,
      dataPointName: sensor.sensor.id,
      lon: sensor.location.longitude,
      lat: sensor.location.latitude,
      dataType: "sensor.community - PM10"
    })
  }

  if(PM25_sensors.includes(sensor_type)) {
    db.dataPoints.create({
      SC_id: sensor.sensor.id,
      dataPointName: sensor.sensor.id,
      lon: sensor.location.longitude,
      lat: sensor.location.latitude,
      dataType: "sensor.community - PM25"
    })
  }

  // increment the count of the sensor type
  sensor_types[sensor_type]++;
}
