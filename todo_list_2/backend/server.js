const express = require('express'),
      bodyParser = require('body-parser'),
      Db = require('./db.js'),
      api = require('./api/routing.js'),
      webapp = require('./webapp/routing.js');

const app = express();

app.use('/to-do-list', webapp);
app.use('/to-do-list/backend', api);

app.use((err, req, res, next) => {
  res.status(400).json(err);
});

app.listen(80, () => {
  console.log('ToDo List listening on port 80!');
});