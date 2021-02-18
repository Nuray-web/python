def welcome():
  print("\n▶   What would you like to do?   ◀\n\nOptions:")
  b = "   1. Show all contacts\n   2. Add new contact\n   3. Request contact\n   4. Delete contact\n   5. Close program\n"
  return b

def add():
  name = str(input("Please enter the name of the contact: "))
  if name in contacts:
    print("\nSorry, this contact is already existing!")
  else:
    num = str(input("Please enter the phone number of the contact: "))
    if num in contacts:
      print("\nSorry, this contact is already exicting!")
    else:
      contacts[name] = num
  return contacts

def remove(): 
  rcont = input("Please enter the contact name you want to delete: ")
  if rcont in contacts:
    ans = str(input("Please, confirm your action. Type 'True' to confirm or 'False' to prevent action."))
    if ans == 'True':
      del contacts[rcont]
      return "\nSuccess, your contact has been deleted!"
    elif ans == 'False':
      print("Your answer is accepted!")
    else:
      print("Excuse me, user, your answer is unreadable!")
  else:
    return ("\nSorry, there's no such contact in phonebook")

def call():
  callcon = str(input("Please enter the name of the contact: "))
  if callcon in contacts:
    return (contacts.get(callcon))
  else:
    return ("\nSorry, there's no such contact in phonebook")

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
  if choice<5:
     while True:
        if choice == 1:
          print(show())
          break
        elif choice == 2:
          print(add())
          break
        elif choice == 4:
          print(remove())
          break
        elif choice == 3:
          print(call())
          break
     return phonebook()
  else: 
    exit()

a = str(input("Please enter your name: "))
print("\n▶   Welcome to the phonebook app, dear, " + a + "   ◀")
contacts = {}
choice = 0
print(phonebook())
