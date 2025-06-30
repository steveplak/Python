def main():

    D,M = CheckParentEyeCLR()
    if D == M:
        print("Your eyes are likely", D)
    elif D == "brown" or M == "brown":
        print("Your eyes are likely brown")
    else:
        print("I dont know")



def CheckParentEyeCLR():
    eye_colours = ["brown","blue","green","hazel","amber","grey","black","violet","red"]

    while True:
        dadclr = input("What is your dad's eye colour? ")

        if dadclr in eye_colours:
            break
        else: 
            print("retry")

        

    while True:
        momclr = input("What is your mum's eye colour? ")

        if momclr in eye_colours:
            break
        else: 
            print("retry")

    return dadclr,momclr




main()