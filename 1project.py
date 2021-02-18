def welcome():
  print("\n▶   Welcome to the phonebook app, dear, User!   ◀")
  print("\n---   What would you like to do?   ---\n\nOptions:")
  print("   1. Show all contacts\n   2. Add new contact\n   3. Request contact\n   4. Delete contact\n   5. Close program\n")
  choice = int(input("Please, enter the num of the option: "))
  return choice

def add():
  name = str(input("Please, enter the name of the contact: "))
  if name in contacts:
    print("\n///   Sorry, this contact is already existing!   ///")
  else:
    num = str(input("Please, enter the phone number of the contact: "))
    contacts[name] = num
  print("\n")
  return contacts

def remove(): 
  rcont = input("Please, enter the contact name you want to delete: ")
  if rcont in contacts:
    ans = str(input("Please, confirm your action. Type 'True' to confirm or 'False' to prevent: "))
    if ans == 'True':
      del contacts[rcont]
      return "\n///   Success, your contact has been deleted!   ///"
    elif ans == 'False':
      return ("\n///   Your answer is accepted!   ///")
    else:
      return ("\n///   Excuse me, user, your answer is unreadable!   ///")
  else:
    return ("\n///   Sorry, there's no such contact in phonebook   ///")

def call():
  callcon = str(input("Please, enter the name of the contact: "))
  if callcon in contacts:
    return (contacts.get(callcon))
  else:
    return ("\n///   Sorry, there's no such contact in phonebook   ///")

def show():
  if bool(contacts) == False:
    return ("\n///   Sorry, your phonebook is empty!   ///")
  else:
    for pair in contacts.items():
      print(pair)
    return " "

#!!!без принта не покажет, не забудь вставить принт!!!
def phonebook():
  choice = welcome()
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
  elif choice>5:
    print("\n///   Sorry, given option is unacceptable!   ///")
    return phonebook()
  else: 
    exit()

contacts = {}
choice = 0
print(phonebook())
