$('document').ready(function () {
    console.log("Document Ready")
    $('.btn1').click(function () {
        console.log('Btn 1 clicked')
        var url = '../../txt_file/rk.txt'
        fetch(url).then(function (response) {
            return response.text();
            console.log(response.text())

        }).then(function (data) {
            console.log(data)
            console.log("Printed")
            return data;

        }).catch(function (err) {
            console.log(err)
        })
    })

    // $('.btn2').click(() => {
    //     let url = '../../txt_file/rk.txts';
    //     fetch(url).then(res => res.text())
    //         .then(data => console.log(data))
    //         .catch(err => console.log("Error Occured " + err))
    // })

    $('.btn2').click(() => {
        let data = {
            name: "Rakib",
            age: 122
        }

        let params = {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                'content-type': 'application/json'
            }
        }

        let url = 'https://jsonplaceholder.typicode.com/posts';
        fetch(url, params).then(res => res.text())
            .then(data => console.log(data))
            .catch(err => console.log("Error Occured " + err))
    })

    $('.btn3').click(() => {
        let url = 'https://jsonplaceholder.typicode.com/users';
        fetch(url).then(res => res.json())
            .then(data => {
                console.log(data)
                var str = ''
                for (i in data) {
                    console.log(data[i])

                    let name = data[i].name;
                    let username = data[i].username;
                    let phone = data[i].phone;

                    console.log(name)
                    console.log(username)
                    console.log(phone)

                    str += `
                        <tr>
                        <td>${name}</td>
                        <td>${username}</td>
                        <td>${phone}</td>
                        </tr>`




                }
                $('.insert_here').append(str)





            })




    })


})