#!/usr/bin/env python

import cgi

# "chmod +x link.py" in order to make the file executable
# the link in http://localhost:8888/link.py will lead to this page
# or play in browser by http://localhost:8888/test_urlencode.py?first=John&last=Smith

form = cgi.FieldStorage()
val1 = form.getvalue('first') # or "val1 = form['first'].value"
val2 = form.getvalue('last')

print "Content-type:text/html"
print
print "<html><title>Test URL Encoding</title><body>"
print "Hello, my name is %s %s." % (val1, val2)
print "</body></html>"

