document.getElementById("codesubmit").onsubmit = function(){
    //NOTE id, created at, updated at, status need to use DBtable
    var username=document.getElementById("username");
    var password=document.getElementById("password");
    var code=document.getElementById("code");

    var formData={      //TODO Return this value to server
        'UserName':this.username.value,
        'PassWord':this.password.value,
        'Code':this.code.value
    };

    var xhttp=new XMLHttpRequest();
    xhttp.onreadystatechange=function(){
        if (this.readyState == 4 && this.status == 200){
            //TODO add post event
        }
    }
    xhttp.open("POST", "./html/output.html", true);
    xhttp.send("http://127.0.0.1:8000/submission");

    console.log(formData.UserName)       //NOTE formData value check...
    console.log(formData.PassWord)
    console.log(formData.Code)
};