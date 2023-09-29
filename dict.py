DICTIONARY 

it's both a datatype(dict) and a data structure ,thats is is a way to organise data like lists 

they have a key (a variable ) and a value ( this can be a number , string , list, boolean value etc.,) pair 

dictionaries arent ordered like lists ( which is next to each other ans canbe accessed index by index) the value can be ordered and can be taken seperately index to index 

eg:
dictionary = {	
	'a':1,
	'x':[1,2,5],
	'b':True 
}
print(dictionary['x'][1])

output:
2

#the avove thing is an item ( an item of a dictonary is enclosed between curly brackets ). but here lists can have many dict as it wants 
eg 
new_list = [{
	'hello':24
	'swallow':[1,2,3]
	'it':True
},
{
	'a'= "hello"
}]
print(new_list[1]['a'][2])

output:
l

#where to use lists and dicts : lists are just some  values with their own indexes but dictionary is unordered but still has seperate variables with their own value which can be easy to access than an index value , thus it makes the lists as a small value holder but a dict as a big value holder as it can be easily accessed with more variables and stores more 

any immutable value can be a key eg : strings and boolian are immutable even numbers but lists are muttable thus lits cannot be used 
we can also overwrite the keys like string variables 

we could also use dict(key=value) insted of using all brackets and the key shuld be a variable not a data type or string eg:dict(name='jonny') this is gonna give {'name'='jonny'}

.get() is used to prevent errors for using an variable which isnt in the dict 

eg user={
	'a':1
}
print(user['b'])
#is gonna give error so we use 

print(user.get('b')) 

output:
none 
#there is no key named 'b', thus to prevent error and continue the program we use .get to give us none value or we can assign an default valur by giving a comma and the value
eg : print(user.get('b',2))
outout :
2

to find wheather a key exists in a dict we use .key function and to find whether a value exists we use .value function eg print('a' in user.key()) this is gonna cheak whether the key 'a' is in the user (which is a dict data structure) and gonna give the output as either true or false 

and similarly we give print('helo' in user.values()) is gonna cheak the values of the user(dict) and gonna give true or false

#.clear is used to re assign the dict as a empty dict ({}) 

#.copy is used to copy the  dictionary

#.pop used to remove the key : value pair by giving.pop('the key that you want to remove') and by printing this the pop returns the vaue of the particular key but actually removes both key and value 

#.popitem removes any last key: value pair from dict 

#.update is used to update a key and its value 
eg 
dictionary = {
	'age':20
}
dictionary.update({'age': 25})

print (dictionary)
output :
{'age': 25}

and to add a new key value pair to the dictionary , we use the same .update method
