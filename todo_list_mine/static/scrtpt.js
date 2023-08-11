const add_button = document.getElementById("theButton")
const data = document.getElementById("info")
const text_field = document.getElementById("text_field")


document.body.addEventListener("click", check_if_button);

function check_if_button(event) {
    var target = event.target;
    if (target.id.indexOf('todos_li_done_button') >= 0) {
        str = target.id
        let id = str.slice(str.lastIndexOf('_') + 1);
        let result = { "id": id, "stat": "done" }
        fetch("http://feldbush.su:8000/receiver",
            {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(result)
            }).then(res => {
                if (res.ok) {
                    console.log(res.value)
                } else {
                    alert("something is wrong")
                }
            })
        document.getElementById(target.parentNode.id).remove();
    }
    if (target.id.indexOf('todos_li_change_button') >= 0) {
        str = target.id
        let id = str.slice(str.lastIndexOf('_') + 1);
        let result = { "id": id, "stat": "change" }
        fetch("http://feldbush.su:8000/receiver",
            {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(result)
            }).then(res => {
                if (res.ok) {
                    console.log(res.json())
                } else {
                    alert("something is wrong")
                }
            })
    }
}



add_button.onclick = async function () {
    let result = { "text": text_field.value, "stat": "new" }
    await fetch("http://feldbush.su:8000/receiver",
        {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(result)
        }).then((response) => {
            return response.json();
        })
        .then((data) => {
            number = data;
            console.log(number)
        });
    var html = '<li class="todos_li" id="' + number + '"><input class="todos_text" value="' + text_field.value + '" readonly id="' + number + '"><input type="button" class="btn btn-secondary"  id="todos_li_done_button_' + number + '" value="Mark Done"><input type="button" class="btn btn-secondary" id="todos_li_change_button_' + number + '" value="Change"></li>'
    document.getElementById('todos_ul').innerHTML += html
    text_field.value = ''
}

text_field.addEventListener('keypress', function (e) {
    var key = e.which || e.keyCode;
    if (key === 13) { // код клавиши Enter
        add_button.click();
    }
});