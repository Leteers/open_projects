const sqlite3 = require('sqlite3').verbose(),
      fs = require('fs');

class Db {
    constructor(dbFile) {
      this.dbFile = dbFile;

      if (!this.dbExists()) {
        this.createDb();
      }

      this.db = new sqlite3.Database(this.dbFile, sqlite3.OPEN_READWRITE);  
    }

    /** 
     * This function checks if db exists in expected location.
     */
    dbExists() {
      return fs.existsSync(this.dbFile);
    }

    /** 
     * If db does not exist, this function will create db file and initialize it with expected tables.
     */
    createDb() {
      fs.openSync(this.dbFile, 'w');

      const db = new sqlite3.Database(this.dbFile, sqlite3.OPEN_READWRITE);  

      db.run(
          `CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
            description TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            position INTEGER NOT NULL
          )`
      )
    }

    /** 
     * Function allows to add task with given description to db
     * @param  {Object} task - description and position of new task which should be added to database
     * @param  {function} onFinish - callback which will be triggered on database instert completion
     */
    createTask(task, onFinish) {
      this.db.run("INSERT INTO tasks (description, position) VALUES (?,?)", [task.description, task.position], onFinish)
    }

    /** 
     * Function allows to read all tasks from db
     * @param  {function} onFinish - callback which will be triggered after when all data is read from db
     */
    readTasks(onFinish) {
      this.db.all("SELECT * FROM tasks ORDER BY position", onFinish)
    }
    
    /** 
     * Function allows to update existing task with given id
     * @param  {number} id - task id, it will be used to find task which values should be updated
     * @param  {Object} completed - task completion value to be set
     * @param  {function} onFinish - callback which will be triggered on database update completion
     */
    updateTaskStatus(id, completed, onFinish) {
      this.db.run("UPDATE tasks SET completed=? WHERE id=?", [completed, id], onFinish)
    }

    /** 
     * Function allows to update position of existing task with given id
     * @param  {number} id - task id, it will be used to find task which values should be updated
     * @param  {number} previousPosition - previous position of task
     * @param  {number} newPosition - new position of task
     * @param  {function} onFinish - callback which will be triggered on database update completion
     */
    updateTaskPosition(id, previousPosition, newPosition, onFinish) {
      this.db.run(
        `UPDATE tasks 
         SET position = CASE
                        WHEN id=$id THEN $newPosition
                        WHEN position>$newPosition THEN position+1
                        WHEN (NOT id=$id) AND position=$newPosition AND $newPosition<$previousPosition THEN position+1
                        WHEN position<$newPosition THEN position-1
                        WHEN (NOT id=$id) AND position=$newPosition AND $newPosition>$previousPosition THEN position-1
                        ELSE position
                        END`,
         { $previousPosition: previousPosition,
           $newPosition: newPosition,
           $id: id }, onFinish)
    }

    /** 
     * Function allows to delete task with given id
     * @param  {number} id - task id, it will be used to find task which should be deleted
     * @param  {function} onFinish - callback which will be triggered on database delete completion
     */
    deleteTask(id, onFinish) {
      this.db.run("DELETE FROM tasks WHERE id=?", id, onFinish)
    } 
}

module.exports = Db;
