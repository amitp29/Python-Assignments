'''
6.	Write a function to print the information in the dictionary(bookstore) 

        
        bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}


BOOKSTORE

'Learning XML', 'Erik T. Ray', '2003', '39.95' 
'Everyday Italian', 'Giada De Laurent is', '2005', '30.00']
 'Harry Potter', 'J K. Rowling', '2005', '29.99']

'''

bookstore={"New Arrivals":{
                "COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],
                "CHILDREN":["Harry Potter", "J K. Rowling","2005","29.99"],
                "WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}


    
def extract(dict):
    x = dict.values()
    y = x[0].values()
    
    for book in y:
        print book



extract(bookstore)

