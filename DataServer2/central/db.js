const { DataStore } = require('notarealdb');

const store = new DataStore('./data');

module.exports = {
   dataPoints:store.collection('dataPoints'),
   ARSOMeritev:store.collection('ARSOMeritev'),
   SCMeritev:store.collection('SCMeritev'),
};