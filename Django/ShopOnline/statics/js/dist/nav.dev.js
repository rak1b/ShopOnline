"use strict";

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
}); // THIS IS FOR ADD CART FUNCTIONALITY

function show_cart(cart) {
  if (cart != null) {
    var sum = 0;

    for (var key in cart) {
      sum = sum + cart[key][0];
      console.log(cart[key][0]);
    }

    $("#all_cart_pc").text(sum);
    $("#all_cart_phn").text(sum);
  }
}

$(document).ready(function () {
  if (localStorage.getItem("cart") == null) {
    var cart = {};
  } else {
    cart = JSON.parse(localStorage.getItem("cart"));
    show_cart(cart);
  }

  $(".add_cart").click(function () {
    // _____This 1 portion will run 1 time because ,we will replace it after click_____
    // 111111111111111111111111111111111111111111
    var id = $(this).attr("id");

    if (cart[id] != undefined) {
      qty = cart[id][0] + 1;
      p_name = $("#name_" + id).text();
      cart[id] = [qty, p_name];
    } else {
      qty = 1;
      p_name = $("#name_" + id).text();
      cart[id] = [qty, p_name];
    }

    localStorage.setItem("cart", JSON.stringify(cart));
    show_cart(cart); // 111111111111111111111111111111111111111111

    var getmycart = JSON.parse(localStorage.getItem("cart")); // btn_id is the clicked button_________

    var btn_id = $(this).attr("id"); //getting the value from localStorage using this clicked button,every button has unique id_____

    var btn_val = getmycart[btn_id][0]; // Replace when click add Cart button______
    // ____unique id created using buttton id___

    $(this).replaceWith("\n        <div class='cart_add_minus'>\n          <button class=\"plus_btn\" id=\"plus_btn_".concat(btn_id, "\">+</button>\n          <p class=\"number_span\" id=\"number_span_").concat(btn_id, "\">").concat(btn_val, "</p>\n          <button class=\"minus_btn\" id=\"minus_btn_").concat(btn_id, "\">-</button>\n        </div>\n      ")); // ((((((((((((((((((((PLus button))))))))))))))))))))
    // _______whenever we click the plus button it will increase the btn_val,as well as in the storage_________

    $("#plus_btn_".concat(btn_id)).click(function () {
      btn_val++;
      cart[btn_id][0] = btn_val;
      localStorage.setItem("cart", JSON.stringify(cart));
      console.log(btn_val);
      $("#number_span_".concat(btn_id)).text(btn_val);
      show_cart(cart);
    }); // ((((((((((((((((((((minus button))))))))))))))))))))

    $("#minus_btn_".concat(btn_id)).click(function () {
      if (btn_val >= 1) {
        btn_val--;
        cart[btn_id][0] = btn_val;
        localStorage.setItem("cart", JSON.stringify(cart));
      }

      console.log(btn_val);
      $("#number_span_".concat(btn_id)).text(btn_val);
      show_cart(cart);
    });
  });
});
$("document").ready(function () {
  $(".clear_cart").click(function () {
    localStorage.clear();
    $("#cart_details").html("<h5 class=\"text-center bg-primary\">Cart Cleared,add new</h5>");
    $("#cart_pr_name").html("");
    $("#cart_pr_price").html("");
    $("#all_cart_pc").text(0);
    $("#all_cart_phn").text(0);
  });
});