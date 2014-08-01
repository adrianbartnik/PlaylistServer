var scWidget = null;

var getSoundcloudData = function(){
  return function(data, textStatus, jqXHR){

    $("#songTitle")[0].setAttribute("value", data.title);
    $("#songURL")[0].setAttribute("value", data.permalink_url);
    $("#plattform")[0].setAttribute("value", 1);
    $("#addTitle").css("background-color", "green");

  }
}

var getYoutubeData = function(url){
  return function(data, textStatus, jqXHR){

    $("#songTitle")[0].setAttribute("value", data.items[0].snippet.title);
    $("#songURL")[0].setAttribute("value", url);
    $("#plattform")[0].setAttribute("value", 0);
    $("#addTitle").css("background-color", "green");
  }
}

$(document).ready(function(){

  SC.initialize({
    client_id: "b4c0cbf752c806f6906499259aa0120b"
  });

  $("#songURL").bind("input", function(event){

    url = $("#songURL")[0].value;

    if(validateYT(url)){
      $.get(
        "https://www.googleapis.com/youtube/v3/videos?id=" + getYTID(url) + "&key=AIzaSyBx6d1tSLUQGAwmIqwPvDC-R9ESGsPI_e8&part=snippet", 
        getYoutubeData(url)
        );
    }

    else if(validateSC(url)){
      $.get(
        "http://api.soundcloud.com/resolve.json?url=" + url + "&client_id=b4c0cbf752c806f6906499259aa0120b",
        getSoundcloudData()
        );
    }
  })

  $(".track[plattform*=0]").click(function(){
    var element = ""
    if(event.srcElement.className=="trackText"){
      element = event.target.parentElement;
    } else{
      element = event.target;
    }
  var link = element.getAttribute("url");
  var pos = link.indexOf('&');
  if (pos > 0)
    link = link.substring(0, pos);
  $("#ytplayer")[0].setAttribute("src", link.replace("watch?v=","embed/"));
  $("#ytplayer")[0].setAttribute("style", "display:inline");
  });

  $(".track[plattform*=1]").click(function(){
    var element = ""
    if(event.srcElement.className=="trackText"){
      element = event.target.parentElement;
    } else{
      element = event.target;
    }

  SC.oEmbed(element.getAttribute("url"), {auto_play: true}, function(oembed){
    console.log("oEmbed response: ", oembed);
    $("#scplayer").html(oembed.html);
    scWidget = SC.Widget($("#scplayer").children()[0]);
    scWidget.bind(SC.Widget.Events.FINISH, function(){alert("test")});
  });
  });

  $("#playAll").click(function(){
    alert("hallo");
  });

});



function validateSC(url){
  var regexp = /^https?:\/\/(soundcloud.com|snd.sc)\/(.*)$/;
  return url.match(regexp) ? true : false;
}

function validateYT(url) {
  var p = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
  return (url.match(p)) ? true : false;
}

function getYTID(url) {
  var p = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
  return (url.match(p)) ? RegExp.$1 : false;
}
