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
        fetch("/receiver",
            {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                },
                body: JSON.stringify(result)
            }).then(res => {
                if (res.ok) {
                } else {
                    alert("something is wrong")
                }
            })
        document.getElementById(target.parentNode.id).remove();
    }
    if (target.id.indexOf('todos_li_change_button') >= 0) {
        str = target.id
        let id = str.slice(str.lastIndexOf('_') + 1);
        document.getElementById(id).removeAttribute('readonly')
        document.getElementById(id).select();
        document.getElementById(id).style.color = "red";
        document.getElementById(id).addEventListener('keypress', function (e) {
            var key = e.which || e.keyCode;
            if (key === 13) { // код клавиши Enter
                let result = { "id": id, "stat": "change", "text": document.getElementById(id).value }
                document.getElementById(id).setAttribute('readonly', 'true')
                document.getElementById(id).style.color = '#A6ADBA';
                fetch("/receiver",
                    {
                        method: 'POST',
                        headers: {
                            'Content-type': 'application/json',
                        },
                        body: JSON.stringify(result)
                    }).then((data) => {
                        number = data;
                    });
            }
        });
        // 
    }
}


add_button.onclick = async function () {
    console.log(text_field.value.length)
    if (text_field.value.length === 0) {
        alert("Length of to do should be at least 1 simbol")
    }
    else {
        let result = { "text": text_field.value, "stat": "new" }
        await fetch("/receiver",
            {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                },
                body: JSON.stringify(result)
            }).then((response) => {
                return response.json();
            })
            .then((data) => {
                number = data;
            });
        var html = '<li class="todos_li" id="todos_li_' + number + '"><input class="todos_text" value="' + text_field.value + '" readonly id="' + number + '"><input type="button" class="btn btn-secondary"  id="todos_li_done_button_' + number + '" value="Mark Done"><input type="button" class="btn btn-secondary" id="todos_li_change_button_' + number + '" value="Change"></li>'
        document.getElementById('todos_ul').innerHTML += html
        text_field.value = ''
    }
}

text_field.addEventListener('keypress', function (e) {
    var key = e.which || e.keyCode;
    if (key === 13) { // код клавиши Enter
        add_button.click();
    }
});