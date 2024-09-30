#swaping the value using dict.
print('\n Swapping between key and value vice-versa')

dict1={'a':10,'b':20,'c':30}
print(f" The given dictionary is : {dict1}")
output={}
for key in dict1:
    value=dict1[key]
    if type(value) not in [set,list,dict]:
        output[value]=key
print(f"After swapping the keys and values:{ output}")
print('\n Below is another program\n')

#WAP to filter the set to have only single value datatype using for loop.

print('Set filteration for single value datatype')
items={15,10.5,7+2j,True,'hello',(2,4)}
print(items,'\n')
for item in items:
    if type(items) in (str,tuple):
        items.remove(item)
print(f"The filtered value for single value datatype in set is: {item} \n")
print('\n Below is another program\n')

#printing no occurance in a string.
print('Printing the no. of occurance of words in a given string.')
string="dont trouble the trouble if you trouble the trouble then trouble will trouble you."
words=string.split()
output={ }
for word in words:
    if word in output:
        output[word]+=1
    else:
        output[word]=1
max_val=max(output.values())
max_word=[]
for key in output:
    value=output[key]
    if value==max_val:
        max_word.append(key)
print(max_word)