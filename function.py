def function_name():
    print("hellow ")

# function_name()          #
def function_name():
    return "hellow world"

datafromfunction = function_name()
print(datafromfunction)




# def                             ==> function keyword [define]
# say_hello                       ===> function name
# name ==> parameter              ==> parameter
# print(f"hellow {name}")         ==>task
# say_hello("omar")               ==> omar is the argument




a, b,c = "osama", "ahmed","ali"

def say_hello(name):
    print(f"hellow {name}")

say_hello("omar")
say_hello("ali")
say_hello("alaa")

###Everything in Python is an object, which means we can pass functions.
# Example
Def twice(f, x):  
    # apply f twice  
    return f(f(x))




def addition(n1,n2):
    print(int(n1)+n2)

addition("9",7)                         #transform 9 ===> int
addition(12,-11)



# example

def addition(n1,n2):

    if type(n1)!=int or type(n2)!=int :
       print("only integers allowed")

    else :
        print(n1+n2)


addition ("100","omar")
addition ("100","1")
addition (100,"omar")
addition (100,1)



# ----------------------------------------------
# --function packing, unpacking, *args----------
# ----------------------------------------------



print(1,2,3,4)


my_list=[1,2,3,4]

print(my_list)                  #unpacking
print(*my_list)                  #packing




def say2_hello(n1,n2,n3):
    peoples = [n1,n2,n3]

    for name in peoples :
        print(f"hello {name}")

say2_hello("omar","ahmed","alaa")



def say2_hello(*peoples):       #معناها اني غير مقيد واقدر اكتب اي عدد من الاسماء

    for name in peoples :

        print(f"hello {name}")

say2_hello("omar","ahmed","alaa","abdo","khaled")



def show_details(*skills):
    for skill in skills :

     print(f"hellow omar your skills is {skill}:")


show_details("html","css")



def show_details(*skills2):
      print(f"hellow omar your skills is :")

      for skill2 in skills2 :
       
       print(skill2)

show_details("html","css")



print("@#$"*22)



# ---------------------------------------
# --function default parameters----------
# ---------------------------------------


def say2_hello( name, age, country):  
    print(f"hellow {name} your age is {age} and your country is {country}")


say2_hello("omar", 20, "egypt")



def say2_hello( name, age, country="unknown"):              #===> it means it doesn't have to be written and the code will not be error 
    print(f"hellow {name} your age is {age} and your country is {country}")


say2_hello("omar", 20 )
say2_hello("omar", 20, "egypt" )


# unknown must be in the end 



# ---------------------------------------
# --function packing =>**, unpacking arguments **kWArgs----------
# ---------------------------------------



def show_skills(**skills) :
    print(type(skills))
    for skill , value in skills.items() :
         print(f"{skill}==>{value}")
# show_skills(css="40%",js="34%")        




dic = {
    "age": 19   ,
    "name":"omar",
    "skills":"js",
    "kji":"40%"
}


# print(**dic)
show_skills(**dic)



# function scope 

# local,global 

x = 1   #global scope

def one() :
       x=2

       print(f"print variable from function scope {x}") 

print(f"print variable from global scope {x}")
one()





# built in function 


x = [1,2,3,4,[]]

if all(x) :

    print("all element is true")

else    :

    print("there at least element is false")






x = [1,2,3,4,[]]

if any(x) :         #==> at least one element true

    print("  is true")

else    :

    print(" is false")


print(bin(100))       #==> He converts it to Pinery
print(bin(2))  


a=1
b=2

print(id(1))
print(id(2))

# id ==> the things that are stored in the memory, and it is not repeated like the national number like this



# sum (iterable, start==>اختياري)

c= [1,10,11,2]

print(sum(c))


# round ==> rounds the number


print(round(12.233344))
print(round(12.533344))
print(round(12.233344,2))


# range(start, end, step)
print(list(range(0)))

print(list(range(12)))

# ==> لو حطينا رقم واحد بس يبقا هو ال end لانه اجباري

print(list(range(0,22,2)))

# print

print("hello omar")
print("hello" ,"omar","hay")
print("hello" ,"omar","hay",sep="@")


# end 
print("first line")
print("second line")


print("first line",end="look at me ")
print("second line")



# abs()   ==> القيمه المطلقه

print(abs(-100))




# pow(base, exponent, modulus)   ==> power 

print(pow(2, 3))

print(pow(2, 3,3))



# modulus==> مش اجباري




# min()   ==>  

print(min(2, 3,3,-1))

print(min("w", "z","o","b"))




# max()   ==>  اكبر حاجه

print(max("w", "z","o","b"))


# slice()
slice
a = ["a","c","j","k","h","d"]

print(a[:2])
print(a[slice(5)])
print(a[slice(2,5)])

#use map with predefined function 

def formattext(text):
    return f"- {text} -"

mytext = ["a","c","j","k","h",1]

myfd= map(formattext, mytext)
# print(myfd)

for name in myfd:
    print(name)


for name in list(map(formattext, mytext)) :
    print(name)



def formattext(text):
    return f"- {text.strip().capitalize()} -"

mytext = ["omar","cat","j","k","h","p      "]

myfd= map(formattext, mytext)
# print(myfd)

for name in myfd:
    print(name)


for name in list(map(formattext, mytext)) :
    print(name)




# use map with labda function

print("+"*19)


def rty(text):
    return f"- {text.strip().capitalize()} -"

mytext = ["omar =","cat","j","k","h","p      "]

myfd= map(rty, mytext)

for name in list(map(lambda text: f"+ {text.strip().capitalize()}+",mytext )):
    print(name)

print("+"*19)

for name in list(filter(lambda text: f"+ {text.strip().capitalize()}+",mytext )):
    print(name)











