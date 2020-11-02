"use strict";

console.log("checkout connected");
$("document").ready(function () {
  cart = JSON.parse(localStorage.getItem("cart")); //   if ($.isEmptyObject(cart)) {
  //     $(".product_check").append(`
  //     <h3 class="text-warning text-center>Your Cart is Empty,Insert items first</h3>
  //     `);

  if ($.isEmptyObject(cart)) {
    console.log("Empty", $.isEmptyObject(cart));
    var _checkout_str = "<p class=\"text-danger text-center\">Your Cart is Empty,Insert items first</p>"; // $("#empty_cart").append(checkout_str);
    // $("#checkout_li").append(`<p class="bg-danger">rakib</p>`);

    $("#checkout_li").append(_checkout_str);
  } else {
    var checkout_str = "";

    for (var item in cart) {
      var pname = cart[item][1];
      console.log(pname);
      var qty = cart[item][0];
      console.log(qty);
      checkout_str += "  \n        <li class=\"list-group-item d-flex justify-content-between align-items-center text-info\">".concat(pname, "\n            <span class=\"badge badge-info badge-pill\">").concat(qty, "</span>\n        </li>");
    }
  }

  $("#checkout_li").append(checkout_str);
});