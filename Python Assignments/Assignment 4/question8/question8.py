#Question 8.  Create a suitable data construct to read the data from an xml document 

import xml.dom.minidom
from xml.dom.minidom import parse

DOMObj = xml.dom.minidom.parse("file.xml")
bookstore = DOMObj.documentElement

if bookstore.hasAttribute("shelf"):
    print "Main Header is : %s" % bookstore.getAttribute("shelf")

#Count the books
books = bookstore.getElementsByTagName("book")

#Print details of the books
for book in books:
    print "Here are the Details of all the BOOKS :- "
    if book.hasAttribute("category"):
        print "Category: %s" % (book.getAttribute("category"))

    title = book.getElementsByTagName('title')[0]
    print "Title: %s" % (title.childNodes[0].data)
    author = book.getElementsByTagName('author')[0]
    print "Format: %s" % (author.childNodes[0].data)
    year = book.getElementsByTagName('year')[0]
    print "Rating: %s" % (year.childNodes[0].data)
    price = book.getElementsByTagName('price')[0]
    print "Description: %s" % (price.childNodes[0].data)
