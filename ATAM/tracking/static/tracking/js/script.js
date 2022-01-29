// let map;
// function initMap() {
//   const mapOptions = {
//     zoom: 16,
//     center: { lat: 24.9180, lng: 67.0971 },
//   };

//   map = new google.maps.Map(document.getElementById("map"), mapOptions);

//   const marker = new google.maps.Marker({
//     // The below line is equivalent to writing:
//     // position: new google.maps.LatLng(-34.397, 150.644)
//     position: { lat: 24.9180, lng: 67.0971 },
//     map: map,
//   });
  // You can use a LatLng literal in place of a google.maps.LatLng object when
  // creating the Marker object. Once the Marker object is instantiated, its
  // position will be available as a google.maps.LatLng object. In this case,
  // we retrieve the marker's position using the
  // google.maps.LatLng.getPosition() method.
  // const infowindow = new google.maps.InfoWindow({
  //   content: "<p>Asset 1 Location:" + marker.getPosition() + "</p>",
  // });

  // google.maps.event.addListener(marker, "click", () => {
  //   infowindow.open(map, marker);
  // });

  


// In this example, we center the map, and add a marker, using a LatLng object
// literal instead of a google.maps.LatLng object. LatLng object literals are
// a convenient way to add a LatLng coordinate and, in most cases, can be used
// in place of a google.maps.LatLng object.
// let map;
// function initMap() {
//   const mapOptions = {
//     zoom: 16,
//     center: { lat: 24.9180, lng: 67.0971 },
//   };

//   map = new google.maps.Map(document.getElementById("map"), mapOptions);

//   const marker = new google.maps.Marker({
//     // The below line is equivalent to writing:
//     // position: new google.maps.LatLng(-34.397, 150.644)
//     position: { lat: 24.9180, lng: 67.0971 },
//     map: map,
//   });
//   // You can use a LatLng literal in place of a google.maps.LatLng object when
//   // creating the Marker object. Once the Marker object is instantiated, its
//   // position will be available as a google.maps.LatLng object. In this case,
//   // we retrieve the marker's position using the
//   // google.maps.LatLng.getPosition() method.
//   const infowindow = new google.maps.InfoWindow({
//     content: "<p>Asset 1 Location:" + marker.getPosition() + "</p>",
//   });

//   google.maps.event.addListener(marker, "click", () => {
//     infowindow.open(map, marker);
//   });
//   if (latlngvalues!==oldlatlngvalues){
  
//     console.log("if chl gya h")
//   animatedMove(marker,0.5,oldlatlngvalues,latlngvalues);
// }
// }
// setInterval(function() {

//   // change the map center
//   map.setCenter(latlngvalues);
//   // change the marker position
//   marker.setPosition(latlngvalues);
//   infowindow.setContent("<p>Asset 1 Location:" + marker.getPosition() + "</p>");
// }, 10000); }  






// // move marker from position current to moveto in t seconds
// function animatedMove(marker, t, current, moveto) {
//   console.log("animate function py value starting",current);
//   var lat = current.lat;
//   var lng = current.lng;
//   console.log(moveto.lat);
//   console.log(current.lat);
//   console.log(moveto.lat-current.lat);
//   var deltalat = (moveto.lat - current.lat) / 100;
//   console.log('deltalat ki value',deltalat);
//   var deltalng = (moveto.lng - current.lng) / 100;
//   var delay = 10 * t;
//   //for (var i = 0; i < 100; i++) {
//     (function(ind) {
//       setTimeout(
//         function() {
//           var lat = marker.position.lat;
//           var lng = marker.position.lng;
//           lat += deltalat;
//           lng += deltalng;
//           latlng = new google.maps.LatLng(lat, lng);
//           console.log(latlng);
//           marker.setPosition(latlng);
//         }, delay * ind
//       );
//     })(i)
//   }
// //}



var map = undefined;
var marker = undefined;
var position = [24.9180, 67.0971];
var latlngvalues=null;
var oldlatlngvalues=null

function initialize() {
    var latlng = new google.maps.LatLng(position[0], position[1]);
    var myOptions = {
        zoom: 10,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map"), myOptions);

    marker = new google.maps.Marker({
        position: latlng,
        map: map,
        //icon:'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYS3q7nqwCWYPmtib883U0z2zm-FhUFXqZIg&usqp=CAU',
        title: "Your current location!",
    });

    // google.maps.event.addListener(map, 'click', function(me) {
    //     var result = [me.latLng.lat(), me.latLng.lng()];
    //     console.log(result);
    //     transition(result);
    // });
}

var numDeltas = 100;
var delay = 10; //milliseconds
var i = 0;
var deltaLat;
var deltaLng;
function transition(result){
    i = 0;
    deltaLat = (result.lat - position[0])/numDeltas;
    deltaLng = (result.lng - position[1])/numDeltas;
    moveMarker();
}

function moveMarker(){
    position[0] += deltaLat;
    position[1] += deltaLng;
    var latlng = new google.maps.LatLng(position[0], position[1]);
    map.setCenter(latlng);
    marker.setPosition(latlng);
    if(i!=numDeltas){
        i++;
        setTimeout(moveMarker, delay);
    }
}

  var socket = new WebSocket('ws://localhost:8000/ws/some_url/');
  socket.onmessage = function(event){ 
    var data = JSON.parse(event.data);
    console.log(data);
    latlngvalues = data;
    
    if (latlngvalues!==oldlatlngvalues && oldlatlngvalues !== null){
      
      console.log("if chl gya h");
      transition(latlngvalues);
};
  console.log(oldlatlngvalues,"check kar rha");
  oldlatlngvalues=latlngvalues;

    };
  

