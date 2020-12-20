login_form = '''
    <div class="login-card">
    <h1>Log-in</h1><br>
        <form method="post">
            <p><input type=text name=login placeholder="Username">
            <p><input type=text name='password' placeholder="Password">
            <p><input type=submit value=Login>
        </form>
    </div>
    '''

def lk(username, pwd):
    return '''
    <div hidden="true" id="card" class="lk-card">
    <h1>Personal page</h1><br>
    <p id="login" username="''' + username + '''" cookie="''' + pwd + '''"></p>
    <p id="main_text"></p>
        <form method="post">
            <p><input type=text name=field placeholder="What do you want to search">
            <p><input type=submit value=Search>
        </form>
    </div>
    '''

head = '''
<head>
  <meta charset="UTF-8">
  <title>Insecure login</title>
    <link rel="stylesheet" href="style.css" media="screen" type="text/css" />
</head>
'''

def in_body(body = "") :
    return "<html>" + head + "<body>" + body + "</body></html>"

def js(script_name) :
    return '''<script src="''' + script_name + '''.js"></script>'''
