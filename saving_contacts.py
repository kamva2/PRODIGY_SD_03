# Author: Kamva Poswa
# 21 June 2024

import sqlite3

def main():
    db = sqlite3.connect("contacts.db")
    #db.execute("create table contacts(Name, Surname, Phone_number, Email_address)")
    
    action = input("what are you here for?(add/view) :").lower()
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
            
        view = input("View the contacts?(Y/N): ").lower()
        
        if view == "yes" or view == "y": 
            table = db.execute("select*from contacts")
            for row in table:
                print(row)
                
    else:
        
        table = db.execute("select*from contacts")
        for row in table:
            print(row)
                
    dele = input("Do you what to delete a contact? (Y/N): ").lower()

    if dele == 'yes' or dele == 'y':

        del_cont = input("which contact do you want to delete?(Email_address/Name/Surname): ").Capitalize()
        value = input("The value of the contact you want to delete?: ")

        query = f"DELETE FROM contacts WHERE {del_cont} = ?"
        db.execute(query, (value,))
        db.commit()
        print("Delete of contact complete!")
    db.close()
    
main()
