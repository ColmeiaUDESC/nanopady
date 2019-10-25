from nanopadyTools import *

try:
    # clear the screen
    os.system("clear")

    print("Welcome to nanopady!\n")
    print("Ctrl+d to exit\n")
        
    # address do dontpad
    endereco = input("Please enter the dontpad address (dontpad.com/address): ")

    # check if the user wants to use hash on the URL
    valid = False
    while(valid == False):
        hashopt = input("Do you use hash for your address? [y,n] ").lower()
        if(hashopt == "y" or hashopt == "n"):
            valid = True
        else:
            print("Enter a valid option!")

    # runs the hash function
    if (hashopt == "y"):

        # clear the screen
        os.system("clear")

        valid = False
        while(valid == False):
            # opcoes de hash
            print("What kind of hash do you use?")
            print("1 - MD5")
            print("2 - SHA1")
            print("3 - SHA256")
            print("4 - SHA512")
            hashopt = int(input())

            # check the users option
            if hashopt == 1:
                endereco = hashlib.md5(endereco.encode()).hexdigest()
                valid = True
            elif hashopt == 2:
                endereco = hashlib.sha1(endereco.encode()).hexdigest()
                valid = True
            elif hashopt == 3:
                endereco = hashlib.sha256(endereco.encode()).hexdigest()
                valid = True
            elif hashopt == 4:
                endereco = hashlib.sha512(endereco.encode()).hexdigest()
                valid = True
            else:
                print("Enter a valid option!")


    write("http://dontpad.com/"+endereco+"/")

except EOFError:
    end()
