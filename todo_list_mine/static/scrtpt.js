const button = document.getElementById("theButton")
const data = document.getElementById("info")
const text_field = document.getElementById("text_field")
var id = $('input.todos_done').attr('id');
var elms = document.getElementsByClassName("todos_done")

for(let i =0; i < elms.length; i++){
    console.log(i);
}





document.body.addEventListener("click", check_if_button);

function check_if_button(event) {
    var target = event.target;
    if (target.id.indexOf('todos_li_done_button')>=0) {
    //     let result = { "text": text_field.value, "stat": "new" }
    //     str=target.id
    //     let id = str.slice(str.lastIndexOf('_')+1);
    //     console.log(id)
    //     fetch("http://127.0.0.1:8000/receiver",
    //     {
    //         method: 'POST',
    //         headers: {
    //             'Content-type': 'application/json',
    //             'Accept': 'application/json'
    //         },
    //         body: JSON.stringify(cars)
    //     }).then(res => {
    //         if (res.ok) {
    //             return res.json()
    //         } else {
    //             alert("something is wrong")
    //         }
    //     })
    
    // }
    // if (target.id.indexOf('todos_li_change_button')>=0) {
    //     str=target.id
    //     let id = str.slice(str.lastIndexOf('_')+1);
    //     console.log(id)
    //     fetch("http://127.0.0.1:8000/receiver",
    //     {
    //         method: 'POST',
    //         headers: {
    //             'Content-type': 'application/json',
    //             'Accept': 'application/json'
    //         },
    //         body: JSON.stringify(cars)
    //     }).then(res => {
    //         if (res.ok) {
    //             return res.json()
    //         } else {
    //             alert("something is wrong")
    //         }
    //     })
    
    }



}








button.onclick = function () {

    let result = { "text": text_field.value, "stat": "new" }
    fetch("http://127.0.0.1:8000/receiver",
        {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(result)
        }).then(res => {
            if (res.ok) {
                return res.json()
            } else {
                alert("something is wrong")
            }
        })
    var html = '<li class="todos_li"><h3 class="todos_text" >'+text_field.value +'</h3><input type="button" class="btn btn-secondary" value="Mark Done"><input type="button" class="btn btn-secondary" value="Change"></li>'
    document.getElementById('todos_ul').innerHTML += html
    text_field.value=''
}

