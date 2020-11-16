$('#form').on('submit', function(e){

e.preventDefault();

  $.ajax({
       type : "POST", 
       url: "{% url 'ajax_posting' %}", /* django ajax posting url  */
       data: {
        first_name : $('#first_name').val(),
        last_name : $('#last_name').val(),
        csrfmiddlewaretoken: '{{ csrf_token }}',
        dataType: "json",

       },
       
       success: function(data){
          $('#output').html(data.msg) /* response message */
       },

       failure: function() {
           
       }


   });


        });     




// $('document').ready(function() {

//     $('.btn1').click(function() {
//         var age = $('.age').val();
        
//         $.ajax(
//         {
//                 type: "GET",
//                 url:'/processView',
//                 data: {
//                 	mage: age
//                 },
//                 success: function(data) {
//                     $(".show_here").html(data)

//                 }
//             }


//         )

//     })
// })




//     $('.btn1').click(function(){
//        var age = $('.age').val();
//     // var catid;
//     // catid = $(this).attr("data-catid");
//     $.ajax(
//     {
//         type:"GET",
//         url: "/processView",
//         data:{
//                 mage: age
//         },
//         success: function( data ) 
//         {
//         	alert(data)
//             // $( '#like'+ catid ).remove();
//             // $( '#message' ).text(data);
//         }
//      })
// });
