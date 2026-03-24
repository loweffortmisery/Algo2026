def split_num_string(A, la, m):
    # A = _a * 10^m + a_
    if (la <= m):
        # A < 10^m
        _a = "0"
        a_ = A
    else:
        _a = A[:(la-m)]
        a_ = A[(la-m):]
    return (_a, a_)
    
def summation(A,B):
    ia = len(A)
    ib = len(B)
    res = ""
    overhead = 0
    while (ia > 0 and ib > 0):
#        print(res)
        ia -= 1
        ib -= 1
        s = int(A[ia]) + int(B[ib]) + overhead
        overhead = s // 10
        s_ = str(s%10)
        res = s_ + res
    while(ia > 0):
#        print(res)
        ia -= 1
        s = int(A[ia]) + overhead
        overhead = s // 10
        s_ = str(s%10)
        res = s_ + res
    while(ib > 0):
#        print(res)
        ib -= 1
        s = int(B[ib]) + overhead
        overhead = s // 10
        s_ = str(s%10)
        res = s_ + res
    if (overhead):
        res = "1"+res

#    if res[0] == "0" and len(res) > 1:
#        print("summation", res, A, B)
    return res


def find_left_non_zero(S, ind):
    for i in range(ind, -1, -1):
        if S[i] != '0':
#            print(f"{S[i]=}")
            return i
    raise ValueError
    
def borrow_to_(S, ind):
    b = find_left_non_zero(S, ind-1)
    #S[b] = str(int(S[b])-1)
#    print(f"{S=}, {b=}, {S[b]=}")
    return b

def subtraction(A,B):
#    print(f"{A=} ------- {B=}")
    ia = len(A)
    ib = len(B)
    if ib > ia:
        raise ValueError
    
    res = ""
    borrowed_from = ia
    while (ib > 0):
        
        ia -= 1
        ib -= 1
        a = int(A[ia])
        if (ia == borrowed_from):
            a -= 1
        b = int(B[ib])
        if (a == 0 and ia > borrowed_from):
            # if we borrowed from some left digit
            # if a != 0 we would borrow from a
            # if we changed a to 0 then ia = borrowed_from, 
            # because we left numbers only when we borrow
            a += 9
        
        if (a < b):
            borrowed_from = borrow_to_(A, ia)
            a += 10
        
        r = a - b
        res = str(r) + res
#        print(f"{res=}, {r=}")

    
    while (ia > 0):
        ia -= 1
        a = int(A[ia])
        if (ia == borrowed_from):
            a -= 1
        if (a == 0 and ia > borrowed_from):
            # if we borrowed from some left digit
            # if a != 0 we would borrow from a
            # if we changed a to 0 then ia = borrowed_from, 
            # because we left numbers only when we borrow
            a += 9
        res = str(a)+res

    fnz = len(res)-1
    for i in range(len(res)):
        if res[i] != "0":
            fnz = i
            break


    return res[fnz:]
    

def karatsuba(A,B):
    if(A == "0" or B == "0"):
        return "0"
    la = len(A)
    lb = len(B)
    if (la < 4 and lb < 4):
        return str(int(A)*int(B))
    n = max(la, lb)
    m = n//2 + n%2
    
    _a, a_ = split_num_string(A, la, m)
    _b, b_ = split_num_string(B, lb, m)

#    print(f"{_a=}, {a_=}, {_b=}, {b_=}")
    z2 = karatsuba(_a, _b) 
#    print(f"{z2=}")
    z0 = karatsuba(a_, b_)
#    print(f"{z0=}")
    z3 = karatsuba(summation(_a, a_), summation(_b, b_))
#    print(f"{z3=}")
    z1 = subtraction(subtraction(z3, z2), z0)
#    print(f"{z1=}")
#    print(f"{z0=}, {z1=}, {z2=}, {z3=}")
    z2_ = z2 + "0"*(2*(m if z2 != "0" else 0))
    z1_ = z1 + "0"*(m if z1 != "0" else 0)
    res = summation(summation(z2_, z1_), z0)
    return res

if __name__ == "__main__":
#    print(subtraction("10000001","10000001"))
#    print(subtraction("10000001","92"))
#    print(subtraction("10010001","200009"))
#    print(subtraction("10000001","239"))
#    print(subtraction("10000001","51242"))
#    print(subtraction("10000001","2"))

    A,B = input().split()
    
#    print(summation("123","123"))
#    print(summation("464","646"))
    
    print(karatsuba(A,B))

