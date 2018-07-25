a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101

print "Value of a & b is ", a & b      # 12 = 0000 1100  (Operator copies a bit to the result if it exists in both operands)

print "Value of a | b is ", a | b;     # 61 = 0011 1101 (It copies a bit if it exists in either operand.)

print "Value of a ^ b is ", a ^ b;     # 49 = 0011 0001 (It copies the bit if it is set in one operand but not both.	)

print "Value of ~a  is ", ~a;          # -61 = 1100 0011 (It is unary and has the effect of 'flipping' bits.	)

print "Value of a << 2 is ", a << 2;   # 240 = 1111 0000 (The left operands value is moved left by the number of bits specified by the right operand.)

print "Value of a >> 2 is ", a >> 2;   # 15 = 0000 1111
