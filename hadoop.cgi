#! /usr/bin/python2
import cgi
import cgitb
cgitb.enable()
print "content-type:text/html"
print ""
html_data=cgi.FieldStorage()
hadoop_version=html_data.getvalue('hd')
if hadoop_version=='hv1'
	print "<meta http-equiv="refresh" content="0;url=file:///var/www/html/option.html" />"
