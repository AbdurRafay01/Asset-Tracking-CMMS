
var map;
var routePolygon = null;      
var directionsDisplay;
var directionsService = new google.maps.DirectionsService();
// Define a symbol using SVG path notation, with an opacity of 1.
var lineSymbol = {
    path: 'M 1.5 1 L 1 0 L 1 2 M 0.5 1 L 1 0',
    strokeOpacity: 1,
    scale: 4,
    strokeColor: "#234099"
    
};
var dashedPolyline = {
    strokeOpacity: 0,
    icons: [{
      icon: lineSymbol,
      offset: '50',
      repeat: '50px'
    }]
};

let icon = {
    url: "https://cdn-icons-png.flaticon.com/512/6395/6395539.png ",
    scaledSize: { width: 55, height: 55 }
  }
  
  
  let position_data = null;
  var counter = 0 ;
  let marker_position = null ;
  let polygon_bounds = null;

  var socket = new WebSocket('ws://localhost:8000/ws/tracking/tracker/1'); 
    socket.onmessage =  function(event){
      var data = JSON.parse(event.data);
      console.log(data);
      console.log(data[0][0]);
      position_data=data
      
      if (counter == 0) {
        initialize();
        console.log(marker_position.position.lat());
        
        console.log(polygon_bounds);
        //if ()
      }
      else{
        //console.log(marker_position.getPosition.lng());
        //console.log(polygon_bounds[1]);
        if (google.maps.geometry.poly.containsLocation(marker_position.getPosition(),polygon_bounds)) {
            //markers[i].setMap(null);
            alert("yes");
        }else{
            alert("no");
        }
        
        //console.log(marker_position);
        //console.log(position_data[0][0], position_data[0][1])
        var latlng = new google.maps.LatLng(position_data[0][0], position_data[0][1]);
        console.log("New location :",latlng);
        marker_position.setPosition(latlng);
        marker_position.setTitle("Asset: 1 "+latlng)
      }
      counter ++; 
    }



function initialize() {
    //var mapCanvas = "map-canvas";
    var mapLat = 30.3753;
    var mapLng = 69.3451;

    var point = new google.maps.LatLng(mapLat, mapLng);

    var mapOptions = {
        zoom: 7,
        center: point,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };
   



    directionsDisplay = new google.maps.DirectionsRenderer({polylineOptions:dashedPolyline});
    var pakistan = new google.maps.LatLng(30.3753, 69.3451);
    var mapOptions = {
        zoom: 7,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        center: pakistan
    }
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    directionsDisplay.setMap(map);
    const marker= new google.maps.Marker({
        position :new google.maps.LatLng(position_data[0][0],position_data[0][1]),
        title :"Asset \n"+new google.maps.LatLng(position_data[0][0],position_data[0][1]),
        map : map,
        icon :icon,
        optimized: false,
      });
      marker_position=marker;
      console.log(marker_position);
      
    calcRoute();
    console.log(polygon_bounds);
    // if (marker.addListener('outside_polygon', () =>
    console.log("initil khatam")
    // )
}

function googleMaps2JTS(boundaries) {
    var coordinates = [];
    var length = 0;
    if (boundaries && boundaries.getLength) length = boundaries.getLength();
    else if (boundaries && boundaries.length) length = boundaries.length;
    for (var i = 0; i < length; i++) {
        if (boundaries.getLength) coordinates.push(new jsts.geom.Coordinate(
        boundaries.getAt(i).lat(), boundaries.getAt(i).lng()));
        else if (boundaries.length) coordinates.push(new jsts.geom.Coordinate(
        boundaries[i].lat(), boundaries[i].lng()));
    }
    return coordinates;
};
var jsts2googleMaps = function (geometry) {
  var coordArray = geometry.getCoordinates();
  //console.log(coordArray);
  var GMcoords = [];
  console.log(GMcoords);
  for (var i = 0; i < coordArray.length; i++) {
    GMcoords.push(new google.maps.LatLng(coordArray[i].x, coordArray[i].y));
  }
  return GMcoords;
}
function calcRoute() {
    var start = document.getElementById('start').innerText;
    console.log(start);
    var end = document.getElementById('end').innerText;
    console.log(end);
    var request = {
        origin: start,
        destination: end,
        travelMode: google.maps.DirectionsTravelMode.DRIVING
    };
    directionsService.route(request, function (response, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
            var overviewPath = response.routes[0].overview_path,
                overviewPathGeo = [];
            for (var i = 0; i < overviewPath.length; i++) {
                overviewPathGeo.push(
                [overviewPath[i].lng(), overviewPath[i].lat()]);
            }

            var distance = 10 / 111.12, // Roughly 10km
                geoInput = {
                    type: "LineString",
                    coordinates: overviewPathGeo
                };
            var geoInput = googleMaps2JTS(overviewPath);
            var geometryFactory = new jsts.geom.GeometryFactory();
            var shell = geometryFactory.createLineString(geoInput);
            var polygon = shell.buffer(distance);
            

            var oLanLng = [];
            var oCoordinates;
            oCoordinates = polygon.shell.points[0];
            for (i = 0; i < oCoordinates.length; i++) {
                var oItem;
                oItem = oCoordinates[i];
                oLanLng.push(new google.maps.LatLng(oItem[1], oItem[0]));
            }
            if (routePolygon && routePolygon.setMap) 
            routePolygon.setMap(null);
            routePolygon = new google.maps.Polygon({
                paths: jsts2googleMaps(polygon),
                map: map
            });
            polygon_bounds= routePolygon; 
        }
    //     var polygonBounds = routePolygon.getPath();
    // var bounds = [];
    // for (var i = 0; i < polygonBounds.length; i++) {
    //       var point = {
    //         lat: polygonBounds.getAt(i).lat(),
    //         lng: polygonBounds.getAt(i).lng()
    //       };
    //       bounds.push(point);
    //  }
      

    //  console.log(polygonBounds);
    //     console.log('polygon',polygon) 
  
    });
}
//google.maps.event.addDomListener(window, 'load', initialize);

