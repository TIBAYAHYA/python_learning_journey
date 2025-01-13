import pyinputplus as pyip,sys 
user_input = "yes"
while user_input == "yes":
    print("do you want to know how to keep an idiot busy? ")
    user_input = pyip.inputYesNo()
    if user_input == "no":
        print("thanks for your time")
        sys.exit