var time = new Date().getTime();
$(document.body).bind("mousemove keypress", function (e) {
    time = new Date().getTime();
    //alert("Czekam na nowe dane!");
});

function refresh() {
    
    if (new Date().getTime() - time >= 60000)
        window.location.reload(true);
    else
        setTimeout(refresh, 10000);
}

setTimeout(refresh, 10000);