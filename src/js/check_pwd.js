function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( "" );
    return xmlHttp.responseText;
}

function redirect_to_login()
{
    window.location.href = common_url + ":" + window.location.port + "/login";
}

function redirect_to_lk()
{
    window.location.href = common_url + ":" + window.location.port + "/lk/" + username;
}


console.log("Login: " + document.getElementById("login"))
console.log("LK: " + document.getElementById("lk"))


var username = document.getElementById("login").attributes.getNamedItem("username").value;
var cookie = document.getElementById("login").attributes.getNamedItem("cookie").value;

var common_url =  window.location.protocol + "//" + window.location.hostname
var url = common_url + ":" + "3000" + "/md5/" + username;

var resp = httpGet(url);
console.log("User " + username + " logged in with password " + cookie + ". Result: " + resp);

if (resp == "No such user") {
    document.getElementById("login").innerHTML = resp;
    alert("User " + username + " doesn't exists");
    redirect_to_login();
} else if (resp == cookie) {
    document.getElementById("login").innerHTML = "Login succeed";
    redirect_to_lk();
} else {
    document.getElementById("login").innerHTML = "Incorrect password";
    alert("Incorrect password");
    redirect_to_login();
}
