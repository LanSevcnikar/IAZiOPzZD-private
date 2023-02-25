<template>
  <div id="app">
    <header>
      <h1>{{ headerTitle }}</h1>
      <button>Button 1</button>
      <button>Button 2</button>
    </header>
    <div class="content">
      <div class="map-container">
        <div class="map"></div>
      </div>
      <div class="info-container">
        <h2>Point Information</h2>
        <ul>
          <li v-for="point in points" :key="point.id" @click="displayPointInfo(point)">
            {{ point.id }}
          </li>
        </ul>
        <div class="info-panel">
          <p>Latitude: {{ activePoint.lat }}</p>
          <p>Longitude: {{ activePoint.lon }}</p>
          <p>ID: {{ activePoint.id }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import topojson from 'topojson-client';

export default {
  name: 'App',
  data() {
    return {
      headerTitle: 'My Website',
      points: [
        { id: 1, lat: 37.7749, lon: -122.4194 },
        { id: 2, lat: 40.7128, lon: -74.0060 },
        { id: 3, lat: 51.5074, lon: -0.1278 }
      ],
      activePoint: {}
    };
  },
  methods: {
    displayPointInfo(point) {
      this.activePoint = point;
    },
    createMap() {
      const width = document.querySelector('.map-container').clientWidth;
      const height = document.querySelector('.map-container').clientHeight;

      const svg = d3
        .select('.map')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

      const projection = d3.geoMercator()
        .translate([width / 2, height / 2])
        .scale(200);

      const path = d3.geoPath()
        .projection(projection);

      const url = "https://raw.githubusercontent.com/deldersveld/topojson/master/world-countries.json";

      d3.json(url).then((data) => {
        console.log(data.objects.countries1);
        const countries = topojson.feature(data, data.objects.countries1);

        svg
          .selectAll('path')
          .data(countries.features)
          .enter()
          .append('path')
          .attr('d', path)
          .attr('fill', '#ccc')
          .attr('stroke', '#fff')
          .attr('stroke-width', 0.5);
      });
    }
  },
  mounted() {
    this.createMap();
  }
};
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

#app {
  height: 100%;
  display: flex;
  flex-direction: column;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.content {
  flex: 1;
  display: flex;
  height: calc(100% - 70px);
}

.map-container {
  flex: 1;
  position: relative;
}

.map {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

.info-container {
  flex: 1;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.info-panel {
  margin-top: 1rem;
  border: 1px solid #ccc;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  padding: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

li:hover {
  background-color: #eee;
}
</style>