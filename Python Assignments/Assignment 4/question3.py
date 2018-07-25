'''
Question 3. Write a program to receive a string from keybord and check if the string has two 'e' in the characters. 
               If yes return True else False.

'''
import re

def check(str):
    
    matchObj = re.search( r'(.*)e(.*)e', str, re.M)
    if(matchObj):
        return True
    return False

value = raw_input('Enter the string : ')


if(check(value)):
    print True
    
else:
    print False
    
