# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List contains Admins.
admins = ["Dodo", "Dina", "Esraa", "Yara", "Fatma", "Bassant", "Enas", "Mai"]

# Login
name = input("Please enter your name ").strip().capitalize()

# If name is in admins.
if name in admins:
    print(f"Hello {name} welcome back")
    option = input("Delete or Update your name ?").strip().capitalize()

    # Update option

    if option == 'Update':

        theNewname = input("please enter your new name ?").strip().capitalize()

        admins[admins.index(name)] = theNewname

        print("Name updated.")

        print(admins)

    # Delete option
        
    elif option == 'Delete':
        
        admins.remove(name)

        print("Name deleted")

        print(admins)  

    else:
        print("Wrong option")    

else:

    status = input("You are not admin, add u? Y, N").strip().capitalize()
    
    if status == 'Yes' or status == 'Y':

        print("You have been added")

        admins.append(name)

        print(admins)

    else:
        
        print("You are not added")

       