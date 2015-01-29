#!/usr/bin/env python

# "chmod +x form.py" in order to make the file executable
# in browser: http://localhost:8888/form.py

print "Content-type:text/html" + \
	"\r\n\r\n" + \
	"<form method=\"post\" action=\"page2.py\">" + \
	"<textarea name=\"name\" cols=\"20\" rows=\"1\">" + \
	"Name ..." + \
	"</textarea>" + \
	"<br/>" + \
	"<textarea name=\"family\" cols=\"20\" rows=\"1\">" + \
	"Family ..." + \
	"</textarea>" + \
	"<br/>" + \
	"<input type=\"submit\" value=\"Submit\">"

import cgi

form = cgi.FieldStorage()
val1 = form.getvalue('birthday')
val2 = form.getvalue('hobby')

print "<br/>Your full birthday and hobby are:<br/>"
print "%s %s" % (val1, val2)



