var get_cart = JSON.parse(localStorage.getItem("cart"));
console.log(get_cart);

// var str = "";
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
  for (let key in get_cart) {
    var product_name = $("#name_" + key).text();
    var price = $("#price_" + key).text();
    total_price = total_price + parseInt(price);
    console.log("total_price =" + total_price + "+" + price);
    var single_price = parseInt(get_cart[key]) * parseInt(price);

    cart_str_name += `
  <li class="text-info">${i++}.${product_name} </li> </br>
`;
    cart_str_price += `<li> ${get_cart[key]}x${price}=${single_price}</li> </br>`;

    $("#cart_pr_name").html(cart_str_name);
    $("#cart_pr_price").html(cart_str_price);
  }
  $("#total_price").text(total_price);
});

// var myHTML = "";

// for (var i = 0; i < 10; i++) {
//   myHTML +=
//     '<span class="test">Testing out my script! loop #' +
//     (i + 1) +
//     "</span><br/><br/>";
// }

// var mytext = "";
// for (var i = 0; i < 10; i++) {
//   mytext +=
//     "<span class='text-danger'>My text:i" + (i + 1) + "</span><br/><br/>";
// }

// // $("#demo").html(myHTML);
// $("#demo2").html(mytext);
// var myVar = JSON.parse(document.getElementById("myVar").value);

// console.log("print", myVar);
// for (i in myVar) {
//   console.log(i);
// }
