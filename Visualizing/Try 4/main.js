const { createApp } = Vue;

const LJUBLJANA_LATITUDE = 46.052;
const LJUBLJANA_LONGITUDE = 14.51;
const STARTING_ZOOM = 13;
const THRESHOLD_DISTANCE = 50;

let app = createApp({
  data() {
    return {
      points: [],
      clusters: [],
      map: null,
      mapLoaded: false,
      selectedCluster: null,
      selectedPoints: [],
      selectedPoint: null,
    };
  },

  // Add a method that is called when mounted
  mounted() {
    // Create the map
    
  },

  methods: {
    createClusters() {
      this.clusters = [];

      function alreadyInCluster(point) {
        let alreadyInCluster = false;
        app.clusters.forEach((cluster) => {
          cluster.points.forEach((clusterPoint) => {
            if (clusterPoint.id === point.id) {
              alreadyInCluster = true;
            }
          });
        });
        return alreadyInCluster;
      }

      // Create a function distance(cluster, cluster) that calculates the distance between two clusters on screen
      function distanceOnScreen(cluster, otherCluster) {
        // 1. find the center of the cluster
        let lat = 0;
        let lng = 0;
        cluster.points.forEach((point) => {
          lat += point.lat;
          lng += point.lng;
        });
        lat /= cluster.points.length;
        lng /= cluster.points.length;
        
        // 2. find the center of the other cluster
        let otherLat = 0;
        let otherLng = 0;
        otherCluster.points.forEach((point) => {
          otherLat += point.lat;
          otherLng += point.lng;
        });
        otherLat /= otherCluster.points.length;
        otherLng /= otherCluster.points.length;
        
        // 3. find the distance between the two centers in the pixels on screen
        let point1 = map.latLngToContainerPoint([lat, lng]);
        let point2 = map.latLngToContainerPoint([otherLat, otherLng]);
        let distance = Math.sqrt(
          Math.pow(point1.x - point2.x, 2) + Math.pow(point1.y - point2.y, 2)
          );
          
        // 4. return the distance
        return distance;
      }

      //  The clusters should be the points themselves if they are far enough apart
      //  But if they are close enough, they should be merged into one cluster
      //  The distance between points is the distance on screen
      
      // loop through all the points and create a cluster for it and add to that all points that are not already in some cluster and are close enough
      this.points.forEach((point) => {
        // loop through all the points and add them to the cluster if they are close enough and are not already in some other cluster
        if (!alreadyInCluster(point)) {
          let cluster = {
            points: [point],
            lat: point.lat,
            lng: point.lng,
          };
          this.points.forEach((otherPoint) => {
            if (!alreadyInCluster(otherPoint) && otherPoint.id !== point.id) {
              if (
                distanceOnScreen(cluster, { points: [otherPoint] }) <
                THRESHOLD_DISTANCE
                ) {
                  cluster.points.push(otherPoint);
                }
              }
            });
            
            // set the cluster lat and lon to be the average of all the points in it
            let lat = 0;
            let lng = 0;
            cluster.points.forEach((point) => {
            lat += point.lat;
            lng += point.lng;
          });
          lat /= cluster.points.length;
          lng /= cluster.points.length;
          cluster.lat = lat;
          cluster.lng = lng;
          this.clusters.push(cluster);
        }
      });

      // loop through all the clusters and create a marker for each one
      this.clusters.forEach((cluster) => {
        // create a marker for the cluster
        let marker = L.marker([cluster.lat, cluster.lng]).addTo(map);
        // Make the marker clickable
        marker.on("click", () => {
          // set the selected cluster to be the cluster that was clicked
          this.selectedCluster = cluster;
        });

        // if the cluster has more than one point, add a popup to the marker
        if (cluster.points.length > 1) {
          marker.bindPopup(`Cluster with ${cluster.points.length} points`);
        }
      });
    },

    addOrRemoveFromSelectedPoints(point) {
      // if the point is already in the selected points, remove it
      if (this.selectedPoints.includes(point)) {
        this.selectedPoints.splice(this.selectedPoints.indexOf(point), 1);
      } else {
        // otherwise add it
        this.selectedPoints.push(point);
      }
    }
  },
}).mount("#app");


let map = L.map("map").setView(
  [LJUBLJANA_LATITUDE, LJUBLJANA_LONGITUDE],
  STARTING_ZOOM
);
console.log("mounted");

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

app.points = [];
// create 30 random points with ids as their number and lat and long the Ljubljana lat and long plus/minus 0.075
for (let i = 0; i < 30; i++) {
  app.points.push({
    id: i,
    lat: 46.052 + Math.random() * 0.15 - 0.075,
    lng: 14.51 + Math.random() * 0.15 - 0.075,
  });
}

map.on('moveend', () => {
  // 1. remove all the markers from the map
  map.eachLayer(layer => {
    if (layer instanceof L.Marker) {
      map.removeLayer(layer)
    }
  })

  // 2. create clusters
  app.createClusters()
})

app.createClusters();