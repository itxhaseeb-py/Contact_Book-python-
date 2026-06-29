print("This is a small program that work as a Contact Book")
print()
Main={
    "Ali": {
        "Phone": "12345",
        "Email": "ali@gmail.com"
    }
}
def add_contact():
    name=input("Enter the name of the contact :").strip().capitalize()
    if name in Main:
        print("Name Already Exist use different name!")
        return None,None
    else :
     phone=input(f"Enter the Phone number of {name} :")
     mail=input(f"Enter the Email of {name} :")
     addres=input(f"Enter the Address of {name} :")

     contact={
        "Phone" : phone,
        "Email" : mail,
        "Address" : addres
     }
     return name ,contact
    
    
def searching_contact():
   name=input("Enter the name for finding the information in Contact Book :").capitalize().strip()
   if name in Main:
      print(Main[name])
   else:
      print("Name not found")
   


def delete_contact ():
   name=input("Enter the contact name you want to delete :").capitalize().strip()
   if name  in  Main:
      Main.pop(name)
      print("Contact deleted")
   else :
      print("Contact not found")




def update_contact():

   nam=input("Enter the contact name for update :").strip().capitalize()
   if nam in Main:   
      nam1=input(f"Do you want to change a single field or to replace the whole contact of {nam}\nif whole contact enter 'Yes' if fied enter 'No' :")
      if nam1.lower() == "yes":
         Main.pop(nam)
         print("Previous contact deleted !")
         name,contact = add_contact()
         if name is not  None and contact is not None:
           Main[name]=contact
      elif nam1.lower() == "no":
         keyy=Main[nam].keys()
         key=input(f"There are the keys of your contact {keyy}\n whcih one you want to update :").strip().capitalize()
         if key in keyy:
            upd=input(f"Enter the updated value for {key} :")
            Main[nam][key]=upd
            print("Value updated")
      else :
         print("Invalid !   just enter (yes / no)")
   else:
    print("Contact not found !")




print("'NOTE :")
print("This is a contact Book that store the Contact 'Name' their Phone_number , Email , Address ")      
print("""
These are the operation that user can perfrom on contact_Book
'add_contact'\n'searching_contact'\n'delete_contact'\n'update_contact'
      """)
print("For exit a program enter 'exit")



while True:
   op=input("Enter the operation you want to perfrom :").lower()
   if op == "add_contact":
     name , contact= add_contact()
     if name is not None and contact is not None :
        Main[name]=contact
      
   elif op == "searching_contact":
      searching_contact()
   
   elif op == "delete_contact":
      delete_contact()
      
   elif op == "update_contact":
      update_contact()
      
   elif op== "exit":
      with open ("Contact_Book.txt" ,"w") as f:
         f.write(str(Main))
      break
   else:
      print("Operation not found")
   
   

print(Main)




# delete_contact()
# print(Main)
# name,contact = Add_contact()
# if name is not  None:
#    Main[name]=contact
# print(Main)

# searching_contact()
    
# update_contact()