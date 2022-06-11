'''
In this program we will see wheather two kangaroos will meet at a point at same time or not.
You have to give starting points and speed(m/jump) of both kangaroos as a input.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
If it is possible, return YES, otherwise return NO.
'''

x1,v1,x2,v2 = list(map(int,input('enter values:').split()))

if x1 > x2:     # It means kangaroo2 is started first.
    # If speed of kangaroo2 is greater than speed of kangaroo1 then only kangaroo2 can catch kargaroo1.otherwise it cann't catch.
    if v2 > v1: 
        if (x1-x2)%(v2-v1) == 0:
            print('yes')
        else:
            print('no')
    else:
        print('no')

elif x2 > x1:       # It menas kangaroo1 is started first.
    if v1 > v2:
        if (x2-x1)%(v1-v2) == 0:
            print('yes')
        else:
            print('no')
    else:
        print('no')
else:
    print('No')

#       INPUT               OUTPUT
# 1817 9931 8417 190          NO
# 0 3 4 2                     YES
# 0 2 5 3                     NO
