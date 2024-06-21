# Author: Kamva Poswa
# 21 June 2024

import sqlite3

def main():
    db = sqlite3.connect("contacts.db")
    #db.execute("create table contacts(Name, Surname, Phone_number, Email_address)")
    
    action = input("what are you here for?(add/view)").lower()
    if action == 'add':
        while True:
            name= input("Enter name: ")
            surname = input("Enter surname: ")
            phone_num = int(input("Enter cellphone number: "))
            email = input("Enter email address: ")
           
            db.execute("insert into contacts(Name, Surname, Phone_number, Email_address) VALUES (?, ?, ?, ?)", (name, surname, phone_num, email))
            db.commit()
            more = input("Do you want to add more Y/N: ").lower()
            if more == "n": break
            
        view = input("View the contacts?(Y/N)").lower()
        
        if view == yes or view == y: 
            table = db.execute("select*from contacts")
            for row in table:
                print(row)
                
        
    else:
        
        table = db.execute("select*from contacts")
        for row in table:
            print(row)
                
       
    db.close()
    
main()