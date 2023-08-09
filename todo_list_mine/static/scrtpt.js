const button = document.getElementById("theButton")
const data = document.getElementById("info")
const text_field = document.getElementById("text_field")
button.onclick= function(){
    let cars ={"text":text_field.value,"stat" : "new"}
    console.log(cars)
    fetch("http://www.feldbush.su:8000/receiver", 
        {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            },
        body:JSON.stringify(cars)}).then(res=>{
                if(res.ok){
                    return res.json()
                }else{
                    alert("something is wrong")
                }
            })
           }
