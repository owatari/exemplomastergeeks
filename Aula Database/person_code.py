from database import db

def new(rooms, beds, balcony, bathroom, window, obs=''):
    quarto = db.Person(rooms=rooms, beds=beds, balcony=balcony,bathroom=bathroom, window=window, obs=obs)
    db.session.add()

def search(id):
    qry = db.session.get(db.Person, id)
    print(f'\tNome: {qry.name} \n\tidade: {qry.age} \n\taltura: {qry.height}cm \n\tcabelo: {qry.hair} \n\tusa oculos: {qry.glasses}')

def delete(id):
    qry = db.session.get(db.Person, id)
    db.session.delete(qry)
    db.session.commit()

def update(id, rooms='', beds='', balcony='', bathroom='', window='', obs=''):
    qry = db.session.get(db.Person, id)
    

# new(2, 2, 1, 2, 5)
search(2)




# def add_person():
#     print("What's their name?")
#     name = input()
#     print("What's their age?")
#     age = input()
#     print("What's their height in centimeters?")
#     height = input()
#     glasses = ''
#     print("Do they use glasses?")
#     while (glasses != True and glasses != False): 
#         glasses = input()
#         if glasses.lower() == 'yes':
#             glasses = True
#         elif glasses.lower() == 'no':
#             glasses = False
#         else:
#             print('Sorry, can you type that again?')
#     print("What's their hair colour?")
#     hair = input()
#     db.session.add(db.Person(name=name, age=age, height=height, glasses=glasses, hair=hair))
#     db.session.commit()

# def remove_person():
#     id = ''
#     while not id.isdecimal():
#         print("What's the ID of the person you want to remove from the database?")
#         id = input()
#         qry = db.session.query(db.Person).filter(db.Person.id == id).first()
#         print(f'Are you sure you want to delete {qry.name} from the database?')
#         if input().lower() == 'yes':
#             db.session.delete(db.session.get(db.Person, id))
#             db.session.commit()
#         else:
#             id = ''

# def search():
#     search = ''
#     while (search.lower() != 'id' and search.lower() != 'name' and search.lower() != 'age' and search.lower() != 'height' and search.lower() != 'glasses' and search.lower() != 'hair'):
#         print("What would you like to search?\n(ID, NAME, AGE, HEIGHT, GLASSES, HAIR)")
#         search = input()
#         if search.lower() == 'id':
#             print("Type the ID you want to search.")
#             qry = db.session.query(db.Person).filter(db.Person.id == input()).all()
#             print('Found '+ str(len(qry)) + ' entry.')
#             for x in qry:
#                 print (f'\tEntry #{x }.\n\t\tName: {x.name.capitalize()}\n\t\tAge: {x.age}\n\t\tHeight: {x.height}cm\n\t\tHair Colour: {x.hair.capitalize()}\n\t\tUses glasses: {x.glasses}')
#         elif search.lower() ==  'name':
#             print("Type the name you want to search.")
#             qry = db.session.query(db.Person).filter(db.Person.name == input()).all()
#             print('Found '+ str(len(qry)) + ' entry.')
#             for x in qry:
#                 print (f'\tEntry #{x }.\n\t\tName: {x.name.capitalize()}\n\t\tAge: {x.age}\n\t\tHeight: {x.height}cm\n\t\tHair Colour: {x.hair.capitalize()}\n\t\tUses glasses: {x.glasses}')
#         elif search.lower() ==  'age':
#             print("Type the age you want to search.")
#             qry = db.session.query(db.Person).filter(db.Person.age == input()).all()
#             print('Found '+ str(len(qry)) + ' entry.')
#             for x in qry:
#                 print (f'\tEntry #{x }.\n\t\tName: {x.name.capitalize()}\n\t\tAge: {x.age}\n\t\tHeight: {x.height}cm\n\t\tHair Colour: {x.hair.capitalize()}\n\t\tUses glasses: {x.glasses}')
#         elif search.lower() ==  'height':
#             print("Type the height you want to search.")
#             qry = db.session.query(db.Person).filter(db.Person.height == input()).all()
#             print('Found '+ str(len(qry)) + ' entry.')
#             for x in qry:
#                 print (f'\tEntry #{x}.\n\t\tName: {x.name.capitalize()}\n\t\tAge: {x.age}\n\t\tHeight: {x.height}cm\n\t\tHair Colour: {x.hair.capitalize()}\n\t\tUses glasses: {x.glasses}')
#         elif search.lower() ==  'glasses':
#             print("Type 'YES' if they use glasses.")
#             qry = ''
#             if input().lower() == 'yes':
#                 qry = db.session.query(db.Person).filter(db.Person.glasses == True).all()
#             else:
#                 qry = db.session.query(db.Person).filter(db.Person.glasses == False).all()
#             print('Found '+ str(len(qry)) + ' entry.')
#             for x in qry:
#                 print (f'\tEntry #{x}.\n\t\tName: {x.name.capitalize()}\n\t\tAge: {x.age}\n\t\tHeight: {x.height}cm\n\t\tHair Colour: {x.hair.capitalize()}\n\t\tUses glasses: {x.glasses}')
#         elif search.lower() ==  'hair':
#             print("Type the hair colour you want to search.")
#             qry = db.session.query(db.Person).filter(db.Person.hair == input()).all()
#             print('Found '+ str(len(qry)) + ' entry.')
#             for x in qry:
#                 print (f'\tEntry #{x}.\n\t\tName: {x.name.capitalize()}\n\t\tAge: {x.age}\n\t\tHeight: {x.height}cm\n\t\tHair Colour: {x.hair.capitalize()}\n\t\tUses glasses: {x.glasses}')

# def update_person():
#     print("Please type the ID of the person you want to update.\nIf you don't know their id you can use our SEARCH function.")
#     qry = db.session.get(db.Person, input())
#     print('Please tell us what would you like to update:\n1 - Name\n2 - Age\n3 - Height\n4 - Hair Colour\n5 - Glasses\nYou can type multiple numbers if you want to edit more than one information.\ne.g: typing 135 will make you edit name, height and glasses.')
#     edt = str(input())
#     if edt.find('1') != -1:
#         var = 0
#         while var == 0:
#             print("What's their new name?")
#             var = input()
#             print("Are you sure you want their new name to be: "+ var +"?")
#             if input().lower() == 'yes':
#                 qry.name = var
#             else:
#                 var = 0
#     if edt.find('2') != -1:
#         var = 0
#         while var == 0:
#             print("What's their new age?")
#             var = input()
#             print("Are you sure you want their new age to be: "+ var +"?")
#             if input().lower() == 'yes':
#                 qry.age = var
#             else:
#                 var = 0
#     if edt.find('3') != -1:
#         var = 0
#         while var == 0:
#             print("What's their new height?")
#             var = input()
#             print("Are you sure you want their new height to be: "+ var +"?")
#             if input().lower() == 'yes':
#                 qry.height = var
#             else:
#                 var = 0
#     if edt.find('4') != -1:
#         var = 0
#         while var == 0:
#             print("What's their new hair colour?")
#             var = input()
#             print("Are you sure you want their new hair colour to be: "+ var +"?")
#             if input().lower() == 'yes':
#                 qry.hair = var
#             else:
#                 var = 0
#     if edt.find('5') != -1:
#         print("Do they still use glasses?")
#         if input().lower() == 'yes':
#             qry.glasses = True
#         else:
#             qry.glasses = False
#     db.session.commit()

