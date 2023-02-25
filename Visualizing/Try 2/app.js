// Define the dimensions of the SVG container
const width = 800;
const height = 600;

// Define the projection and path for the map
const projection = d3.geoMercator()
  .center([10, 50])
  .scale(700)
  .translate([width / 2, height / 2]);
const path = d3.geoPath().projection(projection);

// Define the SVG container
const svg = d3.select('#map')
  .attr('width', width)
  .attr('height', height);

// Load the topojson data for Europe
d3.json('https://raw.githubusercontent.com/deldersveld/topojson/master/world-countries.json').then((data) => {
  // Convert the topojson data to geojson format
  console.log(data);
  const geojson = topojson.feature(data, data.objects.countries1);

  // Draw the map
  svg.selectAll('path')
    .data(geojson.features)
    .enter()
    .append('path')
    .attr('d', path);

  // Define the data for the points
  const points = [
    { name: 'Paris', latitude: 48.8566, longitude: 2.3522 },
    { name: 'Berlin', latitude: 52.5200, longitude: 13.4050 },
    { name: 'Madrid', latitude: 40.4168, longitude: -3.7038 },
    { name: 'Rome', latitude: 41.9028, longitude: 12.4964 },
  ];

  // Draw the points
  svg.selectAll('circle')
    .data(points)
    .enter()
    .append('circle')
    .attr('class', 'point')
    .attr('cx', (d) => projection([d.longitude, d.latitude])[0])
    .attr('cy', (d) => projection([d.longitude, d.latitude])[1])
    .attr('r', 5)
    .on('click', (event, d) => {
      console.log(`Clicked on ${d.name}`);
      // Show additional information here
    });
});
