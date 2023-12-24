# class mo():
#     def __init__(self):
#         print("a new member has been added")   
# mnm = mo()         
# mnm1 = mo()         
# mnm12 = mo()     

# print(mnm.__class__)           # ==> هيجيبلي mnm دي تبع انهي كلاس ====> class mo

print("=+="*22)

# class Omar_elqady():    

#     def __init__ (self):
#         print("hello this course about OOP")

#     def ss(self):
#         print("OOP is very important")


# ww=Omar_elqady()        #بتعمل run تلقائي من غيرما استدعيها
# ww.ss()                 # لازم تتكتب كدة عشان مفيش __init__

print("=+="*22)


# # اي كلمه self يبقا دة inistance

# class Dog():
#     def __init__(self, name1, age1):
#         self.name = name1       # inistance variables الاسم متغير 
#         self.age = age1          # inistance variables السن متغير          
#         print("welcome")       

#     def sit(self):
#         print(self.name + ' is now setting' )

#     def roll_over(self):
#         print(self.name + ' rolled over' )

# dog1=Dog('luci', 4)
# dog1.sit()

# dog2=Dog('koka', 5)
# dog2.sit()

# dog1.roll_over()
# dog2.roll_over()

print("=+="*22)


# class employe():

    # empcount= 0

    # def __init__(self, name1, salary1):
    #     self.name = name1
    #     self.salary = salary1
    #     employe.empcount +=1
    #     print('the employe ',self.name, "is created" )

    # def displaycount(self):
    #     print('total employe %d'% employe.empcount  )
    #     print(f'total employe : {employe.empcount}' )


#     def displayemploye(self):
#         print('name : ', self.name, ', salary: ', self.salary )

# emp1=employe('omar', 22)

# emp1=employe('ahmed', 123)
# emp1=employe('osama', 272)
# emp1.displaycount()
# emp1.displayemploye()



print("=+="*22)

# class member:

#     not_allowed_name = ['hell', 'baloot','shit']                           #انا كدة خليت الاسماء دي محجوزه
#         if self.fname in member.not_allowed_name:
#             print() 

#     users_num = 0

#     @classmethod                                                           #كده نا بعمل class method
#     def show_users_count(cls):                                             #لازم اكتب cls عشان class method
#         print(f'we have {cls.users_num} users in our system')

#     @staticmethod
#     def say_hellow():
#         print('hellow from static method')
 
#     def __init__(self, first_name, middle_name, last_name, gender):          #==> constructor
#         self.fname = first_name                                      #==> attribute
#         self.mname = middle_name                                     #==> attribute
#         self.lname = last_name     
#         self.gender = gender                                         #==> attribute 

#         member.users_num += 1

#     def full_name(self):                                                 #inistance method عشان فيها self
#         if self.fname in member.not_allowed_name:
#             raise ValueError('name not allowed')
#         else:

#             return f"{self.fname} {self.mname} {self.lname}"              #==> method
    
#     def name_with_tittle(self):
#         if self.gender == "male":
#             return f"hello mr / {self.fname} {self.lname}"
        
#         elif self.gender == "female":
#             return f"hello ms / {self.fname} {self.lname}"
        
#         else :
#             return f'hello {self.fname} {self.lname}'
        
#     #مهمه 
#     def get_all_info(self):                 #==> الmetod دي هتعمل عمل الاتنين الي فوق 
#         return f"{self.name_with_tittle()}, your full name is: {self.full_name()} "
    
#     def delete_user(self):                  #==> method بتحدف اليوزر

#         member.users_num -= 1 
#         return f'user {self.fname} {self.mname} {self.lname} Deleted'  



# print(member.users_num)             #==> 0

# member_one = member("omar", 'mohamed', 'elqady', 'male')            #inistance
# member_two = member('ahmed', 'ali', 'helmy','male')                 #inistance
# member_three = member('doaa', 'ali', 'omar', 'female')              #inistance
# member_four = member('shit', 'ali', 'omar', 'female')               #inistance

# print(member.users_num)               #==> 4

# # print(dir(member_two))              #هيطبعلي الname من ضمنهم

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.mname)
# print(member_three.lname)

# print(member_three.full_name())

# print(member_three.name_with_tittle())

# print(member_one.name_with_tittle())

# print("=+="*22)
# print(member_one.get_all_info())
# print(member_three.get_all_info())
# # print(member_four.get_all_info())           #==> error

# # print(dir(member))              #==> method بتاع ال inistance  
# print("=+="*22)

# member.show_users_count()

# print(member_four.delete_user())
# print(member.users_num)

# member.show_users_count()

# print(member_three.delete_user())
# print(member.users_num)

# member.show_users_count()

# member.say_hellow()

# print("=+="*22)
# print("=+="*22)

# # magic method 
# class skill: 
#     def __init__(self):
#         self.skills = ["html", 'css', 'js']

#     def __str__(self):
#         return f'this is my skills ==> {self.skills}'
    
#     def __len__(self):
#         return len(self.skills)

# profile = skill()
# print(profile)        
# print(profile.__class__)        
# print(len(profile))                     

# my_string = 'omar'
# print(type(my_string))
# print(my_string.__class__)
# # print(dir(str))

# print(str.upper(my_string))

# profile.skills.append("php")

# print(len(profile))


















# # inheritance ==> نظام الوراثه

# class food:         #base class
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#         print(f'{self.name} food is created from base class ')

#     def eat(self):
#         print('eat method from base class')



# ####################################


# class apple(food):        #derived class   الي هيورث
    # def __init__(self, name, price, amount):        #over ride علي الي فوق

# #amount دي حاجه خاصه بالكلاس ده ومش مترثه من الي فوق
      
#         # food.__init__(self, name, price)       #create inistance from base class
        # super().__init__(name, price)       #نفس الي فوق بس مش محتاج اكتب اسم الكلاس محتاج اكتب الحاجه الي هورثها فقط
        # self.amount = amount            # *****

        # print(f'{self.name} is created from derived class and price is {self.price} and amount is {self.amount}')


#     def get_from_tree(self):
#         print("get from tree froom derived class")

#     def eat(self):
#         print('eat method from derived class')         # method over ride



# food_one = food('pizza', 130)
# food_one.eat()


# food_two =apple('meat',120 , 990)       


# food_two.eat()              

# food_two.get_from_tree()

