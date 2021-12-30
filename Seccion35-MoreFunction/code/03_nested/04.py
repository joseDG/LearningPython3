


glob1 = 20   # global

def outer():
    outer_loc1 = 30

    def inner():
        #glob1 += 1         # UnboundLocalError
        #outer_loc1 += 1    # UnboundLocalError

        global glob1
        glob1 += 1
        nonlocal outer_loc1
        outer_loc1 += 1

    inner()
    print(outer_loc1)   # 31

outer()
print(glob1)    # 21