def welcome():
  print("\n▶   What would you like to do?   ◀\n\nOptions:")
  b = " 1. Show all contacts\n 2. Request for some contact\n 3. Clear contacts\n 4. Add new contacts\n 5. Delete contacts\n 6. Close program\n"
  return b

def add():
  name = str(input("Please enter the name of the contact: "))
  num = str(input("Please enter the phone number of the contact: "))
  contacts[name] = num
  return contacts

def remove(): 
  rcont = input("Please enter the contact name you want to delete: ")
  if rcont in contacts:
    del contacts[rcont]
    return "\nSuccess, your contact has been deleted!"
  else:
    return ("\nSorry, there's no such contact in phonebook")

def call():
  callcon = str(input("Please enter the name of the contact: "))
  if callcon in contacts:
    return (contacts.get(callcon))
  else:
    return ("\nSorry, there's no such contact in phonebook")

def clear():
  if bool(contacts) == False:
    return "\nSorry, your phonebook is already empty!"
  else:
    contacts.clear()
    return "\nSuccess, your phonebook has been cleared!"

def show():
  if bool(contacts) == False:
    return ("\nSorry, your phonebook is empty!")
  else:
    for pair in contacts.items():
      print(pair)
    return " "

#!!!без принта не покажет, не забудь вставить принт!!!
def phonebook():
  print(welcome())
  choice = int(input("Please enter the num of the option: "))
  while choice != 6:
    if choice == 1:
      print(show())
      break
    elif choice == 4:
      print(add())
      break
    elif choice == 5:
      print(remove())
      break
    elif choice == 2:
      print(call())
      break
    elif choice == 3:
      print(clear())  
      break
    else:
      break
  return phonebook()


a = str(input("Please enter your name: "))
print("\n▶   Welcome to the phonebook app, dear, " + a + "   ◀")
contacts = {}
choice = 0
print(phonebook())
