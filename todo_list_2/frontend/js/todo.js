const backendUrl = "backend/tasks",
      addTaskButton = document.getElementById("add"),
      inputTask = document.getElementById("input-task");

/** 
 * Function to send HTTP requests
 * @param  {string} url
 * @param  {string} method - HTTP method
 * @param  {Object} requestBody - request body in JSON format
 * @param  {string} onFailureMessage - message which should appear in console when request failed
 * @param  {function} onFinish - callback which will be triggered when request is done
 */
function sendRequest(url, method, requestBody, onFailureMessage, onFinish) {
    $.ajax({
        url: url,
        type: method,
        headers: {
            "Content-Type":"application/json"
        },
        data: requestBody
    })
    .done(() => { onFinish(); })
    .fail(() => { console.log(onFailureMessage); })

    return true;
}

/** 
 * ToDo list class
 */
class TodoList {
    /** 
     * Function to change status of task to 'completed'
     * @param  {string} id - id of task which should be updated
     * @param  {function} onFinish - callback which will be triggered after method completed
     */
    completeTask(id, onFinish) {
        const url = backendUrl + "/" + id;
        sendRequest(url, 'PATCH', JSON.stringify({"completed": 1}), "Completed Task Failed", onFinish);
    }

    /** 
     * Function to change status of task to 'uncompleted'
     * @param  {string} id - id of task which should be updated
     * @param  {function} onFinish - callback which will be triggered after method completed
     */
    uncompleteTask(id, onFinish) {
        const url = backendUrl + "/" + id;
        sendRequest(url, 'PATCH', JSON.stringify({"completed": 0}), "Uncompleted Task Failed", onFinish);
    }

    /** 
     * Function to change position of task
     * @param  {string} id - id of task which should be updated
     * @param  {string} previousPosition - current position of task
     * @param  {string} newPosition - position which task should have after update
     * @param  {function} onFinish - callback which will be triggered after method completed
     */
    changeTaskPosition(id, previousPosition, newPosition, onFinish) {
        const url = backendUrl + "/" + id + "/changePosition";
        console.log(url)
        console.log(JSON.stringify({"previousPosition": previousPosition, "newPosition": newPosition}))
        sendRequest(url, 'POST', JSON.stringify({"previousPosition": previousPosition, "newPosition": newPosition}), "Change position Task Failed", onFinish);
    }
    
    /** 
     * Function to add new task
     * @param  {Object} task - object representing new task which should be added
     * @param  {function} onFinish - callback which will be triggered after method completed
     */
    addTask(task, onFinish) {
        sendRequest(backendUrl, 'POST', JSON.stringify(task), "Add Task Failed", onFinish);
    }

    /** 
     * Function to delete task with given id
     * @param  {string} id - id of task which should be deleted
     * @param  {function} onFinish - callback which will be triggered after method completed
     */
    removeTask(id, onFinish) {
        const url = backendUrl + "/" + id;
        sendRequest(url, 'DELETE', null, "Remove Task Failed", onFinish);
    }
    
    /** 
     * Function to get all existing tasks
    */
    allTasks() {
        const response = $.ajax({
            url: backendUrl,
            async: false,
            type: 'GET'
        });

        const parsed_response = JSON.parse(response.responseText);

        return parsed_response;
    }
}

const todoList = new TodoList();

/** 
 * Function to get position of last task
 */

function positionOfLastTask() {
    return Math.max.apply(null, todoList.allTasks().map((task) => { return task.position; }));
}

/** 
 * Function allows to add task with description to ToDo List
 */
function addTask(event) {
    event.preventDefault();
    
    const description = document.getElementById('input-task').value,
          error = document.querySelector(".error").classList;

    let  lastPosition = positionOfLastTask(), 
         currentPosition = Math.max(1, lastPosition + 1);

    if (description === '') {
        error.add("wrong-input");
        return;
    } 
    
    todoList.addTask({'description': description, 'position': currentPosition}, renderTaskList);
    error.remove("wrong-input");
}

/** 
 * Function allows to change task status in ToDo List
 * @param  {Object} task - current task
 */
function changeTaskStatus(task) {   
    if (task.completed == 1) {
        todoList.uncompleteTask(task.id, renderTaskList)
    } else {
        todoList.completeTask(task.id, renderTaskList)
    }
}

/** 
 * Function allows to delete task
 */
function removeTask() {
    const id = this.getAttribute('id');

    todoList.removeTask(id, renderTaskList);
}

addTaskButton.addEventListener('click', addTask);

inputTask.addEventListener('keypress', (e) => {
    if (e.keyCode == 13) {
        e.preventDefault();
        addTaskButton.click();
    }
});

inputTask.addEventListener('focus', () => {
  if (inputTask.value != null)
    inputTask.value = "";
});

/** 
 * Functions to drag and drop tasks
 */

function dragStart(e) {
    this.style.opacity = '0.4';
    prev = this;
    e.dataTransfer.effectAllowed = 'move';
}

function dragEnter(e) {
    this.classList.add('over');
}

function dragLeave(e) {
    e.stopPropagation();
    this.classList.remove('over');
}

function dragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    return false;
}

function drop(e) {
    let id = prev.getAttribute('data-id'),
        previousPosition = prev.getAttribute('data-position'),
        newPosition = e.target.getAttribute('data-position');

    todoList.changeTaskPosition(id, previousPosition, newPosition, renderTaskList); 
}

function dragEnd(e) {
  const listItens = document.querySelectorAll('.single-task');
  [].forEach.call(listItens, (item) => { item.classList.remove('over'); });
  this.style.opacity = '1';
}

/** 
 * Function to render single task
 * @param  {Object} todo - task which should be render
 * @param  {Object} todos - place where rendered task should be added
 */
function renderTask(todo, todos) {

    const li = document.createElement('li');
    li.className = 'single-task';
    li.setAttribute('draggable', "true");
    li.addEventListener('dragstart', dragStart, false);
    li.addEventListener('dragenter', dragEnter, false);
    li.addEventListener('dragover', dragOver, false);
    li.addEventListener('dragleave', dragLeave, false);
    li.addEventListener('drop', drop, false);
    li.addEventListener('dragend', dragEnd, false);
    li.setAttribute('data-position', todo.position);
    li.setAttribute('data-id', todo.id);
    todos.appendChild(li);
    
    const span = document.createElement('span');
    li.appendChild(span);

    const input = document.createElement('input');
    input.id = todo.id;
    input.setAttribute('type', "checkbox");
    input.checked = todo.completed;
    input.addEventListener('click', () => { changeTaskStatus(todo) });
    li.appendChild(input);

    const label = document.createElement('label');
    label.id = todo.id;
    label.className = 'description';
    label.setAttribute('for', todo.id);
    label.innerHTML = todo.description;
    li.appendChild(label);

    const button = document.createElement('button');
    button.id = todo.id;
    button.className = 'remove';
    button.setAttribute('aria-label', "Remove-task");
    button.addEventListener('click', removeTask);
    li.appendChild(button);

    const img = document.createElement('img');
    img.src = 'images/trash.png';
    img.className = 'remove-icon';
    img.alt = 'remove icon';
    button.appendChild(img);
} 

/** 
 * Function to render ToDo List
 */
function renderTaskList() {
    const todos = document.getElementById('todos');
    todos.innerHTML = '';

    for (const todo of todoList.allTasks()) {
        renderTask(todo, todos);
    }
}   

renderTaskList();
