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
