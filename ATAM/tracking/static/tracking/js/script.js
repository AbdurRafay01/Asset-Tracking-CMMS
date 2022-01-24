

  

var latlngvalues=null;
console.log(latlngvalues,"latlng wali")
  var socket = new WebSocket('ws://localhost:8000/ws/some_url/');
  socket.onmessage = function(event){ 
    var data = JSON.parse(event.data);
    latlngvalues = data;
    console.log(data);
console.log(latlngvalues,"dosri")};

// In this example, we center the map, and add a marker, using a LatLng object
// literal instead of a google.maps.LatLng object. LatLng object literals are
// a convenient way to add a LatLng coordinate and, in most cases, can be used
// in place of a google.maps.LatLng object.
let map;
function initMap() {
  const mapOptions = {
    zoom: 16,
    center: { lat: 24.9180, lng: 67.0971 },
  };

  map = new google.maps.Map(document.getElementById("map"), mapOptions);

  const marker = new google.maps.Marker({
    // The below line is equivalent to writing:
    // position: new google.maps.LatLng(-34.397, 150.644)
    position: { lat: 24.9180, lng: 67.0971 },
    map: map,
  });
  // You can use a LatLng literal in place of a google.maps.LatLng object when
  // creating the Marker object. Once the Marker object is instantiated, its
  // position will be available as a google.maps.LatLng object. In this case,
  // we retrieve the marker's position using the
  // google.maps.LatLng.getPosition() method.
  const infowindow = new google.maps.InfoWindow({
    content: "<p>Asset 1 Location:" + marker.getPosition() + "</p>",
  });

  google.maps.event.addListener(marker, "click", () => {
    infowindow.open(map, marker);
  });

setInterval(function() {

  // change the map center
  map.setCenter(latlngvalues);
  // change the marker position
  marker.setPosition(latlngvalues);
  infowindow.setContent("<p>Asset 1 Location:" + marker.getPosition() + "</p>");
}, 30000); }  
