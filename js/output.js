//TODO code result have to output, use innertext

const Http = new XMLHttpRequest();       //NOTE GET.
Http.open('GET', "Manage Server Link");
Http.send();
Http.onreadystatechange = (e) => {
    console.log(Http.responseText);
};

var mysql = required('mysql');        //NOTE DB connection
var db = mysql.createConnection({
    host : "server address",
    user : "user",
    password : "sql pw",
    database : "DB name"
})

// db.connect();

var Check={       //TODO get data have to change with Getdata
    Code_check:"KMG"
}
var inputID=document.getElementById("id")
var inputUsername=document.getElementById("username")
var inputPW=document.getElementById("password")

function click_check(){     //TODO get DB data
    if (inputID==DBid && inputUsername==DBusername){
        if (inputPW==DBpw){
            document.getElementById("check").innerHTML=Check.Code_check
        }
        else{
            alert("비밀번호가 옳지 않습니다.")
        }

    }
    else{
        alert("ID 또는 유저명이 옳지 않습니다.")
    }
}