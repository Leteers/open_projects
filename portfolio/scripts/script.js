const track = document.getElementById("image-track");
const text_begining = document.getElementById("begining_text");
const ending_text = document.getElementById("ending_text");

window.onmousedown = e => {
    track.dataset.mouseDownAt = e.clientX;
}
window.onmousemove = e => {

    if (track.dataset.mouseDownAt === "0") return;
    const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX, maxDelta = window.innerWidth / 2;
    let percentage = (mouseDelta / maxDelta) * -100, nextPercentage = parseFloat(track.dataset.prevPercentage) + percentage;
    nextPercentage = Math.min(nextPercentage, 0);
    nextPercentage = Math.max(nextPercentage, -100);
    track.dataset.percentage = nextPercentage;
    track.animate({ transform: `translate(${nextPercentage}%,-50% )` }, { duration: 1200, fill: "forwards" });
    for (const image of track.getElementsByClassName("image")) {
        image.animate({ objectPosition: `${nextPercentage + 100}% 50%` }, { duration: 1200, fill: "forwards" });
    }
    text_begining.style.opacity = `${nextPercentage * 2 + 100}%`;
    ending_text.style.opacity = `${-nextPercentage * 2 - 100}%`;
}

window.onmouseup = () => {
    track.dataset.mouseDownAt = "0"
    track.dataset.prevPercentage = track.dataset.percentage;
    console.log(track.dataset.percentage);
}





function preventSelection(element) {
    var preventSelection = false;

    function addHandler(element, event, handler) {
        if (element.attachEvent)
            element.attachEvent('on' + event, handler);
        else
            if (element.addEventListener)
                element.addEventListener(event, handler, false);
    }
    function removeSelection() {
        if (window.getSelection) { window.getSelection().removeAllRanges(); }
        else if (document.selection && document.selection.clear)
            document.selection.clear();
    }
    function killCtrlA(event) {
        var event = event || window.event;
        var sender = event.target || event.srcElement;

        if (sender.tagName.match(/INPUT|TEXTAREA/i))
            return;

        var key = event.keyCode || event.which;
        if (event.ctrlKey && key == 'A'.charCodeAt(0))  // 'A'.charCodeAt(0) можно заменить на 65
        {
            removeSelection();

            if (event.preventDefault)
                event.preventDefault();
            else
                event.returnValue = false;
        }
    }

    // не даем выделять текст мышкой
    addHandler(element, 'mousemove', function () {
        if (preventSelection)
            removeSelection();
    });
    addHandler(element, 'mousedown', function (event) {
        var event = event || window.event;
        var sender = event.target || event.srcElement;
        preventSelection = !sender.tagName.match(/INPUT|TEXTAREA/i);
    });

    // борем dblclick
    // если вешать функцию не на событие dblclick, можно избежать
    // временное выделение текста в некоторых браузерах
    addHandler(element, 'mouseup', function () {
        if (preventSelection)
            removeSelection();
        preventSelection = false;
    });

    // борем ctrl+A
    // скорей всего это и не надо, к тому же есть подозрение
    // что в случае все же такой необходимости функцию нужно 
    // вешать один раз и на document, а не на элемент
    addHandler(element, 'keydown', killCtrlA);
    addHandler(element, 'keyup', killCtrlA);
}

preventSelection(document);



window.ontouchstart= e => {
    track.dataset.mouseDownAt = e.clientX;
}
window.ontouchmove = e => {

    if (track.dataset.mouseDownAt === "0") return;
    const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX, maxDelta = window.innerWidth / 2;
    let percentage = (mouseDelta / maxDelta) * -100, nextPercentage = parseFloat(track.dataset.prevPercentage) + percentage;
    nextPercentage = Math.min(nextPercentage, 0);
    nextPercentage = Math.max(nextPercentage, -100);
    track.dataset.percentage = nextPercentage;
    track.animate({ transform: `translate(${nextPercentage}%,-50% )` }, { duration: 1200, fill: "forwards" });
    for (const image of track.getElementsByClassName("image")) {
        image.animate({ objectPosition: `${nextPercentage + 100}% 50%` }, { duration: 1200, fill: "forwards" });
    }
    text_begining.style.opacity = `${nextPercentage * 2 + 100}%`;
    ending_text.style.opacity = `${-nextPercentage * 2 - 100}%`;
}

window.ontouchend = () => {
    track.dataset.mouseDownAt = "0"
    track.dataset.prevPercentage = track.dataset.percentage;
    console.log(track.dataset.percentage);
}