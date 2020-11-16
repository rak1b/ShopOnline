$('document').ready(function() {
    $('.tracker_btn').on('click', function(e) {
        e.preventDefault();
        console.log('Button click')
        let tracker_id = $("#tr_id").val();
        let tracker_email = $("#tr_email").val();
        console.log(tracker_id, tracker_email)
        let url = $(this).attr('data-url')
        let data = {
            tr_id: tracker_id,
            tr_email: tracker_email,
            csrfmiddlewaretoken: $(this).attr('data-csrf'),
            dataType: 'json'
        }

        $.ajax({
            method: 'post',
            url: url,
            data: data,
            success: function(data) {
                console.log(data.msg)
                console.log(data.desc)

                let tr_str = ''
                let desc = data.desc
                if (data.msg === 0) {
                	console.log(data.msg)

                    console.log("O is here")

                     for (i in desc) {
                        console.log(desc[i])
                        tr_str += `
						<p class="badge badge-warning w-50  p-2">
						${desc[i]}</p>
						
						<br>
					

					`
                    }
                } else if (data.msg === 1) {
                	console.log(data.msg)
                    for (i in desc) {
                        console.log(desc[i])
                        tr_str += `
						<p class=" bg-info w-50 mx-auto text-center p-2">
						${desc[i][0]} on <span class="badge badge-warning pl-3">${desc[i][1]}</span></p>
						
					

					`
                    }


                }

                $('.tracker_info').html(tr_str)

            },
            error: function() {
                console.log('Error')
            }
        })
    })
})