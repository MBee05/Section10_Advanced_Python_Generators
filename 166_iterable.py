# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             next(iterator)
#         except StopIteration:
#             break
        
# special_for([1,2,3])

'''<list_iterator object at 0x000002528D35ABF0>
<list_iterator object at 0x000002528D35ABF0>
<list_iterator object at 0x000002528D35ABF0>
<list_iterator object at 0x000002528D35ABF0>
'''
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
        
special_for([1,2,3])

'''<list_iterator object at 0x000001DF971AABC0>
1
<list_iterator object at 0x000001DF971AABC0>
2
<list_iterator object at 0x000001DF971AABC0>
3
<list_iterator object at 0x000001DF971AABC0>  
'''

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break
        
special_for([1,2,3])


'''
<list_iterator object at 0x00000217B48CB910>     
2
<list_iterator object at 0x00000217B48CB910>     
4
<list_iterator object at 0x00000217B48CB910>     
6
<list_iterator object at 0x00000217B48CB910>
'''




class MyGen():
    current =0
    def __init__(self,first, last):
        self.first = first
        self.last = last

    def __iter__(self):
         return self
     
    def __next__(self):
         if MyGen.current < self.last:
             num = MyGen.current 
             MyGen.current +=1
             return num
         raise StopIteration
        

gen = MyGen(0,100)
for i in gen:
    print(i)
    
    
'''
0
1
2
3
4
5
until 99
'''
    
        
        
        