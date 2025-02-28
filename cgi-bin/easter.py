#!/usr/bin/python3
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

year_string = form.getvalue("year")
type = form.getvalue("type")

year = int(year_string)

special_years = ['1954', '1981', '2049', '2076']
specyr_sub = 7
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
  
if year in special_years:
    easter_day = (22 + d + e) - specyr_sub
else:
    easter_day = 22 + d + e

if easter_day > 31:
    easter_day = easter_day - 31
    april = True

verbose_easter = str(easter_day) + {1: '<sup>st</sup>', 2: '<sup>nd</sup>', 3: '<sup>rd</sup>'}.get(4 if 10 <= easter_day % 100 < 20 else easter_day % 10, "<sup>th</sup>")

print("Content-type:text/html; charset=utf-8")
print("")
print("<!DOCTYPE html>")

print("<html lang='en'>")

print("<head>")
print("<link rel='stylesheet' href='../EasterStyle.css'>")
print("<title>Easter</title>")
print("</head>")

print("<body>")
print("The date of Easter Sunday in %s is: " % (year))
print("<br>")

if type == "Verbosely":
    if april == True:
        print("April %s" % verbose_easter)
    else:
        print("March %s" % verbose_easter)
else:
    if april == True:
        print("%s/4/%g" % (easter_day, year))
    else:
        print("%s/3/%g" % (easter_day, year))


print("</body>")
print("</html>")