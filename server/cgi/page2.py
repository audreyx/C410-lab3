#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
val1 = form.getvalue('name')
val2 = form.getvalue('family')

print "Content-type:text/html" + \
	"\r\n\r\n" + \
	"Your full name is:<br/>"
print "%s %s" % (val1, val2)

print "<br/>" + \
	"<form method=\"post\" action=\"page1.py\">" + \
	"<textarea name=\"birthday\" cols=\"20\" rows=\"1\">" + \
	"Birthday ..." + \
	"</textarea>" + \
	"<br/>" + \
	"<textarea name=\"hobby\" cols=\"20\" rows=\"1\">" + \
	"Hobby ..." + \
	"</textarea>" + \
	"<br/>" + \
	"<input type=\"submit\" value=\"Submit\">"

