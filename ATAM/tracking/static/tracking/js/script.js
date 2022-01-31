

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
let icon = {
  url: "https://cdn-icons-png.flaticon.com/512/6395/6395539.png ",
  scaledSize: { width: 55, height: 55 }
}

var marker=[];
var position = [0, 0];
var marker_no=0;
var counter= 1;  
var socket = new WebSocket('ws://localhost:8000/ws/some_url/'); 
  socket.onmessage = function(event){
    var data = JSON.parse(event.data);
    console.log(data);
    if (counter ==1){
    for (i=1;i<=Object.keys(data).length;i++){
       marker[i]= new google.maps.Marker({
        position :new google.maps.LatLng(data[i][i-i], data[i][1]),
        title :"Asset current location",
        map : map,
        icon :icon,
        optimized: false,
      }); //marker initial postion set
      counter ++ ;
       };
       
      }
      else{
    
      marker_no=Object.keys(data);
      marker_no = marker_no[0];
      //console.log(marker_no);
      //console.log(data,{'lat':data[marker_no]['lat']});
      latlngvalues ={'lat':data[marker_no]['lat'],'lng':data[marker_no]['lng']};
      console.log("new value ",latlngvalues);
      console.log("old value",marker[marker_no].getPosition().lat(),marker[marker_no].getPosition().lng());
      transition(latlngvalues,marker_no);
    };
  };
    
    function initialize() {
       
        var latlng = new google.maps.LatLng(24.9812, 67.2313);
        var myOptions = {
            zoom: 8,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map(document.getElementById("map"), myOptions);
    };
    
    var numDeltas = 100;
    var delay = 10; //milliseconds
    var i = 0;
    var deltaLat;
    var deltaLng;

    function transition(result,marker_no){
        //console.log(position); 
        console.log("............",);
        i = 0;
        
        deltaLat = (result['lat'] - marker[marker_no].getPosition().lat())/numDeltas;
        deltaLng = (result['lng'] - marker[marker_no].getPosition().lng())/numDeltas;
        console.log(deltaLat,deltaLng);
        moveMarker(marker_no);
    };
    
    function moveMarker(marker_no){
      lat= deltaLat+marker[marker_no].getPosition().lat() ;
      lng=deltaLng+marker[marker_no].getPosition().lng();
        //console.log(position[0], position[1]);
        var latlng = new google.maps.LatLng(lat, lng);
        //console.log(latlng);
        //console.log(marker_no);
        //console.log(marker[marker_no])  ;
        
        marker[marker_no].setPosition(latlng);

        if(i!=numDeltas){
            i++;
            console.log(i);
            setTimeout(moveMarker,10,marker_no);
        };
        //console.log(marker[marker_no].getPosition().lat(),marker[marker_no].getPosition().lng());
    };
    

