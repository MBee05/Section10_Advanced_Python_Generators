#range(100)# it creates them one by one
#list(range(100)) #list create a geant list over 100 items in memory

#list 
# def make_list(num):
#    result = []
#    for i in range(num):
#        result.append(i*2)
#    return result

# my_list = make_list(100)
# print(my_list)


'''output   [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]        this stays in memory'''




#Everything used as a Generator is iterable but not every iterable is a generator.Generators are actually functions just like range() is a function. Generator functions have yield keyword instead of return keyword in their function.




#generator

# def generator_function(num):
#     for i in range(num):
#         yield i 
#         #yield,pause the function until you ask it to run again 
    
# for item in generator_function(100):
#     print(item)
    
'''0
1
2
3
4
5
6
7
8
9
10....until 99
'''
#it s similar to the list above but its not in memory
        
    
def generator_function(num):
    for i in range(num):
        yield i*2
        
    
g = generator_function(100)
# print(g)

# output create an object in memory
# <generator object generator_function at 0x000002312C254380>

# g = generator_function(100)
# next(g)
# print(next(g))
'''0'''
    
# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))
'''4'''



#Yield keyword pauses the function and comes back to it when it encounters a next keyword. As such it hold only the most recent value of the iterable in the memory. next() can be called until the range provided in our generator function expires. Just as the range expires, if we call out off the range code will throw a Stop Iteration Error.

