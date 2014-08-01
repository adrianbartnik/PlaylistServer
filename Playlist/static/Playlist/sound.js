SC.initialize({
  client_id: "b4c0cbf752c806f6906499259aa0120b"
});

$(document).ready(function(){
  jQuery("#loadTracks").click(function(){
    SC.get("/tracks", {limit: 1}, function(tracks){
      var track = tracks[0];
      SC.oEmbed(track.uri, document.getElementById("track"));
    });
  });
});
