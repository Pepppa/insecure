login_form = '''
        <form method="post">
            <p><input type=text name=login>
            <p><input type=password name='password'>
            <p><input type=submit value=Login>
        </form>
        '''


def in_body(body = "") :
    return "<html><body>" + body + "</body></html>"

def js(script_name) :
    return '''<script src="''' + script_name + '''.js"></script>'''
