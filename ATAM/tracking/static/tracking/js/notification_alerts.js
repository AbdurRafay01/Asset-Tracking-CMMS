
console.log("<<<<<Notifcation alerts>>>>>")



var socket = new WebSocket("ws://localhost:8000/notification_alert/")

socket.addEventListener("message", function (event) {
    let data = JSON.parse(event.data);
    console.log('Message from server', data["status"]);
    if (data["status"]) {
        document.getElementById("alert_icon").style.color = "red";
    } else {
        document.getElementById("alert_icon").style.color = "black";
    }
})

