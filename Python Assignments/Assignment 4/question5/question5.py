#5.	Write a code to read  the data from 
                    #input file called input.txt and 
                    #count the number of characters per line, 
                    #number of words per line and 
                    #write these into output file called as output.txt 
                
char_count_list = []
word_count_list = []
file_input = open('input.txt')

for line in file_input:
    #Counting Starts from here
    char_count = len(line)
    word_count = len(line.split())
    #Counting Ends here
    char_count_list.append(char_count-1)
    word_count_list.append(word_count)

#Writing into output.txt file
file_output = open('output.txt','w+')
for row in range(line_count):
    file_output.write('line %s has %s total characters with number of words being %s \n\n' %(row+1, char_count_list[row], word_count_list[row]) )
    
file_output.close()
