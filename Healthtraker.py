def getdate():
    import datetime
    return datetime.datetime.now()



while True:
    list = ["1.Harry",
            "2.Rohan",
            "3.Hammad",
            "4.Harsh"]
    print("Eneter your choice or enter '0' for exit:")
    print(list)
    ch = int(input())
    if ch==1 :

        while True:
            print("Harry's Log:")
            print("Eneter your choice:")
            print("Press 1 for Diet")
            print("Press 2 for Exercise")
            print("Press 0 for Exit")
            ch1 = int(input())
            if ch1==1:
                Data = input("Type here:\n"+str([str(getdate())])+":")
                with open("Harrylog.txt","a") as f:
                    f.write(str([str(getdate())])+":"+Data+"\n")
                    print("Data submitted successfully")

            elif ch1 == 2 :
                Data = input("Type here:\n" + str([str(getdate())]) + ":")
                with open("Harryexercise.txt", "a") as f:
                    f.write(str([str(getdate())]) + ":" + Data + "\n")
                    print("Data submitted successfully")

            elif ch1 == 0 :
                break

            else:
                print("Please enter valid choice")

    elif ch==2 :
        while True:
            print("Rohans's Log:")
            print("Eneter your choice:")
            print("Press 1 for Diet")
            print("Press 2 for Exercise")
            print("Press 0 for Exit")
            ch2 = int(input())
            if ch2==1:
                Data = input("Type here:\n"+str([str(getdate())])+":")
                with open("Rohandiet.txt","a") as f:
                    f.write(str([str(getdate())])+":"+Data+"\n")
                    print("Data submitted successfully")
            elif ch2 == 2 :
                Data = input("Type here:\n" + str([str(getdate())]) + ":")
                with open("Rohanexercise.txt", "a") as f:
                    f.write(str([str(getdate())]) + ":" + Data + "\n")
                    print("Data submitted successfully")

            elif ch2 == 0 :
                break

            else:
                print("Please enter valide choice")



    elif ch==3 :
        while True :
            print("Hammad's Log")
            print("Eneter your choice:")
            print("Press 1 for Diet")
            print("Press 2 for Exercise")
            print("Press 0 for Exit")
            ch3 = int(input())
            if ch3==1:
                Data = input("Type here:\n"+str([str(getdate())])+":")
                with open("Hammaddiet.txt","a") as f:
                    f.write(str([str(getdate())])+":"+Data+"\n")
                    print("Data submitted successfully")
            elif ch3 == 2 :
                Data = input("Type here:\n" + str([str(getdate())]) + ":")
                with open("Hammadexercise.txt", "a") as f:
                    f.write(str([str(getdate())]) + ":" + Data + "\n")
                    print("Data submitted successfully")
            elif ch3 == 0:
                break
            else:
                print("Please enter valid choice")



    elif ch==4 :
        while True:
            print("Harsh's Log")
            print("Enter your choice:")
            print("Press 1 for Diet")
            print("Press 2 for Exercise")
            print("Press 0 for Exit")
            ch4 = int(input())
            if ch4==1:
                Data = input("Type here:\n"+str([str(getdate())])+":")
                with open("Harshdiet.txt","a") as f:
                    f.write(str([str(getdate())])+":"+Data+"\n")
                    print("Data submitted successfully")
            elif ch4 == 2 :
                Data = input("Type here:\n" + str([str(getdate())]) + ":")
                with open("Harshexercise.txt", "a") as f:
                    f.write(str([str(getdate())]) + ":" + Data + "\n")
                    print("Data submitted successfully")

            elif ch4 == 0:
                break

            else:
                print("Please enter valid choice")


    elif ch==0:
        break



    else:
        print("Please enter valid choice")