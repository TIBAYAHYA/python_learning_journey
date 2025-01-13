birthday_diction = {"alice":"15 jan","mahmoud":"15dec","camelo":"20april"}
while True:
    print("please enter a name(or blank to quit)")
    inputed_name = input()
    if inputed_name == " ":
        break
    if inputed_name in birthday_diction:
        print(birthday_diction[inputed_name]+"is the birthday of "+inputed_name)
    else:
        print("I have no data base of that person's birthday")
        print("can you tell me what his birthday")
        birthday_diction[inputed_name] = input()
        print("data base updated!")
        