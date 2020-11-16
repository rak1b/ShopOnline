// $('document').ready(function(){
//     $('.btn_click').click(function(){
//         const xhr = new XMLHttpRequest();
//         xhr.open('GET','../txt_file/rk.txt',true);
//         xhr.onreadystatechange=function(){
//             if(xhr.readyState==XMLhttpRequest.DONE){
//                 if(xhr.status==200){
//                     console.log(xhr)
//                     console.log(xhr.responseText)
//                 }else{
//                     console.log("Error")
//                 }
//             }
//         }

//         xhr.send();

//     })
// })

$('.btn_click').click(function () {
    console.log("Button Clicked")
    const xhr = new XMLHttpRequest();
    // xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1', true)
    xhr.open('POST', 'http://dummy.restapiexample.com/api/v1/create', true)
    xhr.getResponseHeader('content-type', 'json')
    // xhr.open('GET', '../txt_file/rk.txt', true);

    xhr.onprogress = function () {
        console.log("On Progress")
    }

    xhr.onreadystatechange = function () {
        console.log(xhr.readyState)
    }

    xhr.onload = () => {
        if (this.status == 200) {
            console.log("Data Sent Successfully")
        }
        else {
            console.error("Failed To sent data")
        }
        console.log(this.responseText)
        console.log("Everything loaded")
    }

    var values = { "name": "test1", "salary": "1a23", "age": "23" }
    xhr.send(values);
})


$('.btn_get').click(function () {
    console.log("Button Get Clicked")
    const xhr = new XMLHttpRequest();
    // xhr.open('GET', 'http://dummy.restapiexample.com/api/v1/employees', true)
    xhr.open('GET', 'https://api.mocki.io/v1/ce5f60e2', true)
    // xhr.open('POST', 'http://dummy.restapiexample.com/api/v1/create', true)
    // xhr.getResponseHeader('content-type', 'json')
    // xhr.open('GET', '../txt_file/rk.txt', true);

    xhr.onload = function () {
        if (this.status == 200) {
            let data = JSON.parse(this.responseText);
            for (i in data) {
                // console.log(i)
                console.log(data[i])
            }
        }
        else {
            console.error("Failed To sent data")
        }
        console.log(this.responseText)
        console.log("Everything loaded")
    }

    var values = { "name": "test1", "salary": "1a23", "age": "23" }
    xhr.send(values);
})