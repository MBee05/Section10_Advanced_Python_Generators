def fib(num):
   a=0
   b=1
   for i in range(num):
       yield a
       temp=a
       a = b
       b = temp + b

for x in fib(20):       

    print(x)

'''
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
'''


# list 

def fib2(num):
   a=0
   b=1
   result =[]
   for i in range(num):
       result.append (a)
       temp=a
       a = b
       b = temp + b
   return result

print(fib2(100))
