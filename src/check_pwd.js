var username = document.getElementById("login").attributes.getNamedItem("username").value;
var cookie = document.getElementById("login").attributes.getNamedItem("cookie").value;

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

var common_url =  window.location.protocol + "//" + window.location.hostname
var url = common_url + ":" + window.location.port + "/md5/" + username;
var resp = httpGet(url);

if (resp == "No such user") {
    document.getElementById("login").innerHTML = resp;
    alert("User " + username + " doesn't exists");
    redirect_to_login();
} else if (resp == cookie) {
    document.getElementById("login").innerHTML = "Login succeed";
} else {
    document.getElementById("login").innerHTML = "Incorrect password";
    alert("Incorrect password");
    redirect_to_login();
}
