import time
import os 
save = []
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")
class Gym:
    def __init__(self, first_name, last_name, id, status="inactice"):
        self.first_name= first_name
        self.last_name= last_name
        self.id= id
        self.status= status
        save.append(self)
    def show(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nMembership ID: {self.id}\nMembership Sstatus: {self.status}\n{"_"*20}" 

def ask():
    name1=input("Enter first name: ").lower()
    name2=input("Enter last name: ").lower()
    id=input("Enter membership ID: ")
    status=input("Enter membership status or click enter to skip: ").lower()
    if status == "active" : status = "active"
    else : status = "inactive"
    return Gym(name1, name2, id, status)

def search_helper(attr,val):
   found = False
   clear_screen()
   for member in save:
     if getattr(member, attr) == val:
        print("Member Found:") 
        print(member.show())
        found = True
   if not found:
      print("Not found!\n")

while True:
   print("Welcome To Gym Membership Management 🦾\n\n")
   print("Choose an Action:\n1. Add new member\n2. Display all members\n3. search for a member\n4. Exit\n")
   choice = input("Enter your choice: ")
   if choice == "1" :
       clear_screen()
       x = ask()
       print("Member added successfully ◘") ; time.sleep(4) ; clear_screen()

   elif choice == "2" :
       clear_screen()
       print("Display all members...") ; time.sleep(2)
       for s in save:
           print(s.show())

   elif choice == "3" :
       clear_screen()
       print("Search by:\n\n1. Membership status\n2. First Name\n3. Membership ID")
       choice=input("Enter your choice: ")
       if choice == "1" :
           while True:
             search = input("Enter the membership status to search: ").lower()
             if search not in ["active","inactive"] : print("Please enter (Active/Inactive) only") ; continue
             search_helper("status",search)
             break
           
       elif choice == "2" :
           search = input("Enter the first name to search: ").lower()
           search_helper("first_name",search)

       elif choice == "3" :
           search = input("Enter the membership ID to search: ")
           search_helper("id",search)

       else : 
           clear_screen()
           print("Invalid Input\nPlease enter (1/2/3) only!")

   elif choice == "4" :
       clear_screen() ; print("Thanks for using our app\nExiting...") ; time.sleep(2) ; break
   
   else:
       print("Invalid Input\nPlease enter (1/2/3/4) only!\n")