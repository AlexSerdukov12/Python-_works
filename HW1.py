# alex serdukov , 323274787 #
import math
import string

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

def RemoveMinDigit(Number):
    new_num,mul=0,1
    min_digit=int(min(str(Number)))
    lengh_of_number=len(str(Number))
    for i in range (lengh_of_number):
        if(Number%10 != min_digit):
            new_num += int(Number % 10)* mul
            mul*=10
            Number = int(Number / 10)
        else:
            Number/=10
    return(new_num)


def SquareArea(a,b,c,d,alfha,beta):
    s=(abs(a)+abs(b)+abs(c)+abs(d))/2
    k=math.sqrt((s-a)*(s-b)*(s-c)*(s-d)-0.5*a*b*c*d*(1+math.cos(math.radians(alfha)+math.radians(beta))))
    return k




def CheckArithmeticSeries(Number):
    ArrayNumbers=str(Number)
    Numerical_difference= Number%10 - (Number/10-Number%10*0.1)%10
    for i in range(len(str(Number))-1):
        if(int(ArrayNumbers[i+1])-int(ArrayNumbers[i]) != Numerical_difference):
            return False

    return  True




def CanBeTriangle(a,b,c):

    if(a>0 and  b>0 and  c>0):
        if(a<b+c and  b<a+c and  c<a+b):
            return True
    return False




def CalcUpperCalcLower(my_Array):
    Number_of_Upper_cases=0
    Number_of_Lower_cases=0
    for i in my_Array:
        if(i.islower() == True):
            Number_of_Lower_cases += 1

        if(i.isupper() == True):
            Number_of_Upper_cases+=1

    print("Number_of_Upper_cases={0} \nNumber_of_Lower_cases={1}".format(Number_of_Upper_cases,Number_of_Lower_cases))


def xnor(a,b):
    if(a==b):
        return True
    return False


def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True



print("xnor is =",xnor(1,2))
print("new number after remove min digit = ",RemoveMinDigit(98715023510))
print("SquareArea=",SquareArea(4,5,4,5,90,90))
print("CheckArithmeticSeries = ",CheckArithmeticSeries(1234567))
print("CanBeTriangle=", CanBeTriangle(3.333, 4.444, 5.555))
CalcUpperCalcLower("This is a WONDERFUL Day")
print("the number is perfect? : " , perfect_number(6))
string = "This is a wonderful day"
if (ispangram(string) == True):
    print("the sting is pangram")
else:
    print("the sting isnt pangram")
