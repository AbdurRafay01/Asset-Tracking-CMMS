
let icon = {
  url: "https://cdn-icons-png.flaticon.com/512/6395/6395539.png ",
  scaledSize: { width: 55, height: 55 }
}

var marker=[];
var position = [0, 0];
var marker_no=0;
var counter= 1;  
var socket = new WebSocket('ws://localhost:8000/current_location/'); 
  socket.onmessage =  function(event){
    var data = JSON.parse(event.data);
    console.log(data);
    if (counter ==1){
    for (i=1;i<=Object.keys(data).length;i++){
       marker[i]= new google.maps.Marker({
        position :new google.maps.LatLng(data[i][i-i], data[i][1]),
        title :"Asset "+i+"\n"+new google.maps.LatLng(data[i][i-i], data[i][1]),
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
      console.log(data[marker_no]);
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
    
    var numDeltas = 1;
    var delay = 10; //milliseconds
    var i = 0;
    var deltaLat;
    var deltaLng;

    function transition(result,marker_no){
        //console.log(position); 
        console.log("............",);
        i=0;
        
        deltaLat = +(((result['lat'] - marker[marker_no].getPosition().lat())/numDeltas).toFixed(4));
        
        deltaLng = +(((result['lng'] - marker[marker_no].getPosition().lng())/numDeltas).toFixed(4));
        console.log(deltaLat,deltaLng);
        moveMarker(marker_no);
    };
    
    function moveMarker(marker_no){
      lat= +((deltaLat+marker[marker_no].getPosition().lat()).toFixed(4)) ;
      lng=+((deltaLng+marker[marker_no].getPosition().lng()).toFixed(4));
      console.log(lat,lng);
        var latlng = new google.maps.LatLng(lat, lng);
        //console.log(latlng);
        //console.log(marker_no);
        //console.log(marker[marker_no])  ;
        
        marker[marker_no].setPosition(latlng);
        marker[marker_no].setTitle("Asset"+marker_no+latlng);
        // if(i!=numDeltas){
        //     i++;
        //     console.log(i);
        //     setTimeout(moveMarker,5,marker_no);
        // };
      
        
        //console.log(marker[marker_no].getPosition().lat(),marker[marker_no].getPosition().lng());
    };
    
