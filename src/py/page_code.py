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
    <div class="lk-card">
    <h1>Personal page</h1><br>
    <p id="lk" username="''' + username + '''" cookie="''' + pwd + '''"></p>
    <p>
    All the Linux/C error codes are listed below.

I occasionally google C error codes, but always end up grepping through /usr/include to find the answer. To save myself, and a few others, some time in the future...

/usr/include/asm-generic/errno-base.h

#ifndef _ASM_GENERIC_ERRNO_BASE_H
#define _ASM_GENERIC_ERRNO_BASE_H

#define EPERM        1  /* Operation not permitted */
#define ENOENT       2  /* No such file or directory */
#define ESRCH        3  /* No such process */
#define EINTR        4  /* Interrupted system call */
#define EIO      5  /* I/O error */
#define ENXIO        6  /* No such device or address */
#define E2BIG        7  /* Argument list too long */
#define ENOEXEC      8  /* Exec format error */
#define EBADF        9  /* Bad file number */
#define ECHILD      10  /* No child processes */
#define EAGAIN      11  /* Try again */
#define ENOMEM      12  /* Out of memory */
#define EACCES      13  /* Permission denied */
#define EFAULT      14  /* Bad address */
#define ENOTBLK     15  /* Block device required */
#define EBUSY       16  /* Device or resource busy */
#define EEXIST      17  /* File exists */
#define EXDEV       18  /* Cross-device link */
#define ENODEV      19  /* No such device */
#define ENOTDIR     20  /* Not a directory */
#define EISDIR      21  /* Is a directory */
#define EINVAL      22  /* Invalid argument */
#define ENFILE      23  /* File table overflow */
#define EMFILE      24  /* Too many open files */
#define ENOTTY      25  /* Not a typewriter */
#define ETXTBSY     26  /* Text file busy */
#define EFBIG       27  /* File too large */
#define ENOSPC      28  /* No space left on device */
#define ESPIPE      29  /* Illegal seek */
#define EROFS       30  /* Read-only file system */
#define EMLINK      31  /* Too many links */
#define EPIPE       32  /* Broken pipe */
#define EDOM        33  /* Math argument out of domain of func */
#define ERANGE      34  /* Math result not representable */

#endif
    </p>
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
