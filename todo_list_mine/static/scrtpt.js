const button = document.getElementById("theButton")
const data = document.getElementById("info")
const text_field = document.getElementById("text_field")
var id = $('input.todos_done').attr('id');
var elms = document.getElementsByClassName("todos_done")

for(let i =0; i < elms.length; i++){
    console.log(i);
}

button.onclick = function () {

    let cars = { "text": text_field.value, "stat": "new" }
    fetch("http://127.0.0.1:8000/receiver",
        {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(cars)
        }).then(res => {
            if (res.ok) {
                return res.json()
            } else {
                alert("something is wrong")
            }
        })
    var html = '<li class="todos_li"> <h3 class="todos_li_text">'+text_field.value+'</h3><input type="button" class="todos_li_delete_button">Send</input></div>'
    document.getElementById('todos_ul').innerHTML += html
    text_field.value=''
}

