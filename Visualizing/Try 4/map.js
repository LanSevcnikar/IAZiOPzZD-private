

const map = L.map('map').setView([46.052, 14.51], 13);

const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

let points = []
// create 30 random points with ids as their number and lat and long the Ljubljana lat and long plus/minus 0.075
for (let i = 0; i < 30; i++) {
  points.push({
    id: i,
    lat: 46.052 + Math.random() * 0.15 - 0.075,
    lng: 14.51 + Math.random() * 0.15 - 0.075
  })
}
createClusters()

