$(document).ready(function(){
  $(".target").bind("input", function(event){
    if(validateYT($("#inputtext")[0].value)){
      $("#ytplayer")[0].setAttribute("src", $("#inputtext")[0].value.replace("watch?v=","embed/"));
      $("#ytplayer")[0].setAttribute("style", "display:inline");
    }
  })
});

function validateYT(url) {
  var p = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
  //return (url.match(p)) ? RegExp.$1 : false;
  return (url.match(p)) ? true : false;
}
