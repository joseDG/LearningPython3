
val = 71.01234567890123456789012345678901234567890123456789

print(val)                      #71.01234567890124 ==> 14 decisimal precision printed
print('{:20}'.format(val))      #   71.01234567890124 ==> total 20 output units, right-aligned
print('{:11f}'.format(val))     #  71.012346 ==>  print 11 units. Use default precision (typically 6)
print('{:11.3f}'.format(val))   #     71.012 ==> 11 output units, 3 of them precision
print('{:3.5f}'.format(val))    #71.01235 ==> 5 precision. It will have more priority
print('{:.8f}'.format(val))     #71.01234568 ==> 8 precision. No specific alignments
#print('{.8f}'.format(val))     #AttributeError


val = 2.67
print(val)                     #2.67
print('{:11f}'.format(val))    #   2.670000 ==>  trailing zeros  : 11 output units (6 is precision)
print('{:11.2f}'.format(val))  #       2.67   (.2f use 2 precision)
print('{:11.1f}'.format(val))  #        2.7   rounding
print('{:11.0f}'.format(val))  #          3   rounding

print('{:11.0f}'.format(2.5))  #          2   rounding to 2
print('{:11.0f}'.format(-2.5))  #        -2   rounding to -2

# {value:width.precision}