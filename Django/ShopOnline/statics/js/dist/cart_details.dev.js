"use strict";

var get_cart = JSON.parse(localStorage.getItem("cart"));
console.log(get_cart); // var str = "";
// $(document).ready(function () {
//   for (let key in get_cart) {
//     console.log(`Product ${key}:${get_cart[key]}`);
//     str += `
//     ${key}: ${get_cart[key]} </br>
//   `;
//   }
//   $("#demo").html(str);
// });
// var product_name,
//   cart_str = "";
// $(document).ready(function () {
//   for (let key in get_cart) {
//     product_name = $(`#name_pr${key}`).html();
//     cart_str += `
//     <li class="text-info">${product_name}: ${get_cart[key]} </li> </br>
//   `;
//   }
//   $("#cart_li").html(cart_str);
// });

var product_name,
    cart_str_name = "";
var cart_str_price = "";
var get_cart = JSON.parse(localStorage.getItem("cart"));
var total_price = 0;
console.log("printing get_cart", get_cart);
var i = 1;
$(document).ready(function () {
  for (var key in get_cart) {
    var product_name = $("#name_" + key).text();
    var price = $("#price_" + key).text();
    var qty = get_cart[key][0];
    console.log(qty);
    console.log("total_price =" + total_price + "+" + price);
    var single_price = parseInt(qty) * parseInt(price);
    total_price = total_price + single_price;
    cart_str_name += "\n  <li class=\"text-info\">".concat(i++, ".").concat(product_name, " </li> </br>\n");
    cart_str_price += "<li> ".concat(qty, "x").concat(price, "=").concat(single_price, "</li> </br>");
    $("#cart_pr_name").html(cart_str_name);
    $("#cart_pr_price").html(cart_str_price);
  }

  $("#total_price").text(total_price);
});