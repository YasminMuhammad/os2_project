import random
class Team :
    def __init__(self , name , sec , department ):
        self.name = name
        self.sec = sec
        self.department= department
        
        
def members ():
    member1 = Team("Ahmed Abd El-Maksoud Ahmed " , 4 , "CS")
    member2 = Team("Hazem Ahmad Ahmad Rady" , 2 , "CS") 
    member3 = Team("Mostafa Eid Abd El-Khalek " , 4 , "CS")
    member4 = Team("Hadeer Kandeel Abd El-Ghaffar " , 4 , "CS")
    member5 = Team("Yasmin Muhammad Abdullah" , 4 , "CS")
    
    print("Team members ")
    
    print("1 ")
    print(member1.name , "    sec : " , member1.sec , "  " , member1.department)
    
    print("2 ")
    print(member2.name , "         sec : " , member2.sec , "  " , member3.department)

    print("3 ")
    print(member3.name , "     sec : " , member3.sec , "  " , member3.department)

    print("4 ")
    print(member4.name , "  sec : " , member4.sec , "  " , member4.department)

    print("5 ")
    print(member5.name , "        sec : " , member5.sec , "  " , member5.department)

print("")
members()
print("")
print("Our program takes the length of the password and generates a random password of the same length ")

password_len = int(input("Enter the length of password : "))
All_words="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(All_words,password_len ))
print("")
print("Generated password is :  " ,password)
