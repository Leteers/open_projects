const express = require('express'),
      validate = require('express-validation'),
      Validation = require('./validation.js')
      bodyParser = require('body-parser'),
      Db = require('./../db.js');
      
const dbFile = "db.db";
const database = new Db(dbFile);

const api = express();

api.use(bodyParser.json());

/** 
 * Read all tasks
 */
api.get('/tasks', (req, res, next) => {
  database.readTasks((err, result) => {
    if (err) next(err)
    else res.json(result)
  });  
})

/** 
 * Create new task
 */
api.post('/tasks', validate(Validation.addingTaskSchema), (req, res, next) => {
  database.createTask(req.body, (err, result) => { 
    if (err) next(err)
    else res.status(201).end()
  });
})

/** 
 * Delete task with given id
 */
api.delete('/tasks/:id', (req, res, next) => {
  database.deleteTask(req.params.id, (err, result) => {  
    if (err) next(err)
    else res.end()
  });  
})

/** 
 * Update status of task with given id
 */
api.patch('/tasks/:id', validate(Validation.updateStatusOfTaskSchema), (req, res, next) => {
  database.updateTaskStatus(req.params.id, req.body.completed, (err, result) => { 
    if (err) next(err)
    else res.end()
  });  
})

/** 
 * Change position of task with given id
 */
api.post('/tasks/:id/changePosition', validate(Validation.changePositionOfTaskSchema), (req, res, next) => {
  let body = req.body;

  database.updateTaskPosition(req.params.id, body.previousPosition, body.newPosition, (err, result) => { 
    if (err) next(err)
    else res.end()
  }); 
})

module.exports = api;
