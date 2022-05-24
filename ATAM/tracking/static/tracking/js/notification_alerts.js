// console.log("<<<<<Notifcation alerts>>>>>")



var notification_socket = new WebSocket("ws://localhost:8000/notification_alert/")

notification_socket.onmessage = function (event) {
    var data = JSON.parse(event.data)
    // console.log("Printing data " + event.data)
    // console.log(typeof event.data);
    // console.log(typeof data);

    // console.log(data['msg'][0]['fields'])
    // console.log("checking len")
    // console.log(data['msg'].length)
    const no_of_tracker_outside = Object.keys(data['msg']).length

    if (no_of_tracker_outside > 0) {
        for (let index = 0; index < no_of_tracker_outside; index++) {
            Object.entries(data['msg'][index]['fields']).forEach(([key, val]) => {
                // console.log(key + " " + val); // the name of the current key.
            });
        }
    }


    if (no_of_tracker_outside > 0) {
        document.getElementById("alert_icon").style.color = "red";
        document.getElementById("notification_list_item").style.color = "red"
    } else {
        document.getElementById("alert_icon").style.color = "white";
        document.getElementById("notification_list_item").style.color = "black";
    }
}

// socket.addEventListener("message", function (event) {
//     let data = JSON.parse(event.data);
//     console.log('Message from server', data["status"]);
//     if (data["status"]) {
//         document.getElementById("alert_icon").style.color = "red";
//     } else {
//         document.getElementById("alert_icon").style.color = "black";
//     }
// })