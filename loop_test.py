#Get the Enviromnment from the User and print it on the Screen

for i in range(5):
    env = input("Enter the Environment: ") #taking input from the user (keyboard) in env variable
    print("The Environment is:", env)

    #Conditional Statement Simple - if -else
    if env == "prod":
        print("Don't Deploy on Friday")
    elif env == "stg":
        print("Take backup and test well before deploy")
    elif env == "test":
        print("test it well")           
    else:
        print("Safe to Deploy any day")