var username = document.getElementById("login").attributes.getNamedItem("username").value;
var cookie = document.getElementById("login").attributes.getNamedItem("cookie").value;

var common_url =  window.location.protocol + "//" + window.location.hostname
var url = common_url + ":" + "3000" + "/md5/" + username;

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
var resp = httpGet(url);
console.log("User " + username + " logged in with password " + cookie + ". Result: " + resp);

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
