def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x, n-1)

"""
For this implementation (x=2, n=5) , the trace is

power(2, 5)    returns 16*2  = 32
    power(2,4)       returns 8*2 = 16
        power(2,3)     returns 4*2 = 8
            power (2,2)     returns 2*2 = 4
                power (2,1)   returns 2*1 = 2
                    power (2,0) returns 1


The arrows would trace downwards for the calls and upwards for the returns as in the textbook

"""


print(power(2,5))
