stringVariable = "hello";
strinSingleQuote = 'Strings can have single quotes';

#print(stringVariable);

def myPrintMethod (myParameter):
    print(myParameter)
    print('World') 

myPrintMethod('Puta')

def myMultiplyMethod(arg1, arg2):
    return  arg1 * arg2

print(myMultiplyMethod(5, 3))

grades = [5, 10, 25, 30, 35]
tupla = (5, 10, 25, 30, 35) # The tuple is inmutable 
setOfgrades = {5, 10, 25, 30, 35, 35} #unique and unordered

set1 = {1,2,3,4,5}
set2 = {1,3,5,7,9,11}

print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))