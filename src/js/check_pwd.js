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

function getLoginElement()
{
    if (document.getElementById("lk") == null) {
        return document.getElementById("login");
    } else {
        return document.getElementById("lk");
    }
}

element = getLoginElement();
console.log("Login element: " + element + " " + element.id);

var username = element.attributes.getNamedItem("username").value;
var cookie = element.attributes.getNamedItem("cookie").value;

var common_url =  window.location.protocol + "//" + window.location.hostname
var url = common_url + ":" + "3000" + "/md5/" + username;

var resp = httpGet(url);
console.log("User " + username + " logged in with password " + cookie + ". Result: " + resp);

if (resp == "No such user") {
    element.innerHTML = resp;
    alert("User " + username + " doesn't exists");
    redirect_to_login();
} else if (resp == cookie) {
    if (element.id == "login" ) {
        alert("Login succeed");
        document.getElementById("card").hidden = false;
        element.id = "lk";
    }
} else {
    element.innerHTML = "Incorrect password";
    alert("Incorrect password");
    redirect_to_login();
}
