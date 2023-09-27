"""LISTS:

just like functions (like int,float list etc) we have some specific methods that we could perform on lists 

these methods can be used bykeeping a dot after the list and typing in the method eg (list.method)

square brackets are used to ndicate lists and commas are used between the items to indicate a seperate item (index) in the list 

now lets name a list as a basket which is  : basket = [1,2,3,4,5]

methods doesnt perform an action (eg : type conversion ) but its gonna change the entire list 

eg : for adding something to the list ( it adds the new item to the end of the list ), the method "append" is used"""

basket = [1,2,3,4,5]
new_basket = basket.append(23)
print(new_basket)

'''output: 
none '''

'''this is because append is not a function and its a method which means it changes/"modifyies" the the list 'basket' and not changes the basket just to assign it to the new_basket 
but now if you just give '''

basket.append(23)
new_basket=basket
print(basket)
print(new_basket)
'''outout:
[1,2,3,4,5,23]
[1,2,3,4,5,23]'''

'''after performing the method on the list  we could assign that list to some other variables and both the new list and the list on which the method used contains same values / items in the list'''

#similar to append the method'index' is used to add an item to the list but this could add that to any index we want eg:

basket = [1,2,3,4,5]
#         0 1 2 3 4  these are the indexes for the list"basket"
basket.insert(4,100)
#insert(which index spot should the new item to be placed in , whats the item to be placed
print(basket)

#output : [1,2,3,4,100,5]

#similarly the method extend could also be used but we could actually assign some variables while performing the function eg: new_basket = basket.extend([100]) , it adds the item at end 

#for removing something from list .pop is used to remove the item ,by giving the index of the item to be removed "basket.pop(indexes like 0 , 1 )" and simply basket.pop() removes end item

'''just like pop the method remove is used , but here we will give the item to be removed not the index of item to be removed eg: list=['my','name'] then list.remove('my')will modify list into the value list = ['name']'''

#the only assignable methods ate extend and pop as if we assign and print the list.pop(index) then pop returns /prints the thing that is removed 

#.clear method is used to remove everything and clear the entire basket 

#a method called .index is used to locate at which index the object is in eg 
new_list=['a','b','c','d']
print(new_list.index('d'))

#output:3
#we could also add (start and stop) from where(index) to where(index) to search for the index eg : newl=_list.index('d',0,4) its gonna give the same output 

#to cheak wheather something is in the given list or string we use the method .in is used the result is given either true or false  eg 
newlist=[1,2,3,4]
print(1 in newlist)

#output : true same could be used in strings eg : print('i' in 'hi my name is ') will give output as true 

#.count can be used to cound , how many times the value occures in the given list 

#.sort is a method that can be used to sort / modify the list in a particular sequence and sorted() is a function form of .sort which doesnt modify the actual list 
#eg : list=[1,2,4,3] list.sort() or sorted(list) will give output as [1,2,3,4]

#just like string slicing lists can also be sliced in the same way

#.copy is used to copy the list or assign it to anither variable 

#.reverse is used to reverse the list which is same as using list[::-1]

#one of the most useful function in lists are the len() function which gives us the number of items in the list

'''another useful thing is called range function eg:you want to print/assign a long list with numbers in a particular sequence you can use list(range(starting value,ending value , steap over value))'''

#.join() IS A FUNCTION LIKE method that  can be used on strings to add additional things in a STRING eg : string=' ' ,print(string.join(['hi,'my','name','is',]) is goanna giv hi my name is


#LIST UNPACKING
'''jsut like how we assign multiple values to a string eg: a,b,c =1,2,3 the same we can do in list a,b,c=[1,2,3] and another feature is assigning a variable with a * before to to assign remaining vaues for list eg : a,b,c,*other = [1,2,3,4,5,6,7] then print(other) gives [4,5,6,7]and if we give a,b,c,*other,d = [1,2,3,4,5,6,7] then print(other) gives [4,5,6] and d value is assigned to the last item ( here 7)

'''sometimes the methods results is given as none which indicated an absence of value , its a keyword and can be used to assign to variables just like how we assign '' in strings for an upcoming variable '''
