command=""
flag=0
while  True:
    command=input(">").lower()
    if command=="start":
        if flag==1:
            print("car is already  started...")

        else:
            print("car is  started...")
            flag=1
    elif command=="stop":
        if flag==0:
            print("car is already stopped...")

        else:
            print("car is  stopped...")
            flag=0
    elif command=="quit":
        break
    else:
        print("""
        i think you need some help...
        start-to start the car
        stop-to stop the car
        quit-to quit
        """)
