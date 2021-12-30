


glob1 = 20   # global

def outer():
    outer_loc1 = 30
    x = 15          # another outer local

    def inner():
        inner_loc = -5
        x = 7       # another inner local
        print(inner_loc)    # -5
        print(x)            # 7: is it in my local scope? Yes, use it
        print(outer_loc1)   # 30: local? No. Enclosing? Yes, use it
        print(outer_loc2)   # 40: local? No. Enclosing? Yes, use it
        print(glob1)        # 20: local? no, enc? no, global? Yes, use

    outer_loc2 = 40
    inner()
    print(x)    # 15: local? yes, use it. inner x has no effect

outer()