$(document).ready(function () {
  $(".caro").lightSlider({
    item: 4,
    loop: true,
    keyPress: true,
    pager: false,
    auto: true,
    loop: true,
    pauseOnHover: true,
    slideMove: 2,
    easing: "cubic-bezier(0.25, 0, 0.25, 1)",
    speed: 600,
    responsive: [
      {
        breakpoint: 1920,
        settings: {
          item: 6,
          // slideMove: 2,
          // slideMargin: 6,
        },
      },
      {
        breakpoint: 1000,
        settings: {
          item: 5,
        },
      },
      {
        breakpoint: 780,
        settings: {
          item: 4,
          slideMove: 1,
        },
      },
      {
        breakpoint: 480,
        settings: {
          item: 2,
          slideMove: 1,
        },
      },
    ],
  });
});

if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
}

$(".add_cart").click(function () {
  console.log("clicked");
  var id = $(this).attr("id").toString();
  console.log(id);
  console.log(cart[id]);
  if (cart[id] != undefined) {
    cart[id] = cart[id] + 1;
  } else {
    cart[id] = 1;
  }
});
