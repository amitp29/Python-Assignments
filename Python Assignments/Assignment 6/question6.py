class Matrix(object):
    def __init__(self, values):
        self.__values = values
 
    def setValues(self, values):    
        self.__values = values
 
    def getValues(self):
        return self.__values
 
    def __add__(self, other_matrix):
        matrix = []
        for row_num in range(2):
            row = []
            for col_num in range(2):
                value = self.__values[row_num][col_num] + other_matrix.__values[row_num][col_num] 
                row.append(value)
                
            matrix.append(row)   
        return Matrix( matrix)
        
m1 = Matrix([[1,0],[3,0]])
print(m1.getValues())
 
m2 = Matrix([[0,-2],[0,-4]])
print(m2.getValues())
 
m3 = m1 + m2 # This became possible because we have overloaded + operator by adding a    method named __add__

print(m3.getValues())
