import re 

file_input = open('IP-Interface-input.txt')

for line in file_input:    
    if( len(line.split()) == 5):
        remove_spaces = re.sub(r'\s+', " ", line)
        next_col = re.search( r'(.*?) (.*) YES (.*?) (.*)' , remove_spaces)
  
        if next_col:
            print "\n%s, %s "%(next_col.group(1),next_col.group(3))
           
    if( len(line.split()) == 6):
        remove_spaces = re.sub(r'\s+', " ", line)
        next_col = re.search( r'(.*?) (.*) YES (.*?) (.*?) (.*)' , remove_spaces)
                
        if next_col:
            print "\n%s, %s %s "%(next_col.group(1),next_col.group(3), next_col.group(4))
