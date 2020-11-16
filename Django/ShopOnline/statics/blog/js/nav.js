// THIS IS FOR PHONE NAVBAR FUNCTIONALITY
$(".three_dot").click(function () {
  $(".resp_nav").toggle(function () {
    $(".resp_nav").width("100%");
  });
});
$(document).ready(function () {
  $("#cart_icon").click(function () {
    console.log("cart clicked");
  });
});