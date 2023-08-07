const express = require('express'),
      path = require("path");

const webapp = express(),
      frontendDirPath = path.join(__dirname, '/../../frontend/');

webapp.use('/style', express.static(path.join(frontendDirPath, 'style')));
webapp.use('/images', express.static(path.join(frontendDirPath, 'images')));
webapp.use('/js', express.static(path.join(frontendDirPath, 'js')));

webapp.get('/frontend', (req, res) => {
  const indexHtmlPath = path.join(frontendDirPath, 'index.html');
  res.sendFile(indexHtmlPath);
});

module.exports = webapp;
