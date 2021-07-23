def myFilter(L,func):
    new_list=[]
    for i in L:
        if(func(i)==True):
            new_list.append(i)

    return new_list


def myFilterMult(L,funcL):
    new_list=[]
    x=funcL[0]
    y=funcL[1]
    for i in L:
        if(x(i) and y(i)):
            new_list.append(i)

    return new_list


def myPrime(x):
    for i in range(2,x):
        if x%i ==0:
            return False
    else:
        return True


def isPalindrome(x):
    number=str(x)
    rev_number= number[::-1]
    if ( number == rev_number ):
        return True
    return False


def is_anagram(str1, str2):

    first_string=str1
    first_string=first_string.lower()
    first_string=sorted(first_string)

    second_string=str2
    second_string=second_string.lower()
    second_string = sorted(second_string)

    return (first_string==second_string)



y = myFilter([9,10,16,24, 29, 36,11],myPrime)
print(y)
x = myFilterMult([1,9,10,16,24,55, 131,149,181],[myPrime,isPalindrome])
print(x)

print("School master and The classroom is_anagram:",is_anagram('School master','The classroom'))
print("Elior and roli is_anagram:",is_anagram('Elior','roli'))
