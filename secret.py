

def pegasus():

    level_system = True
    print("\n*******************************************************************" +
          "\nWe are team PEGASUS, commissioned by Aniket, Austin, and Chandra." +
          "\nYour goal is to decrypt this message, and find what the secret is.")

    def new_level(original_message, encrypted_message):
        print("\n\nThis is the encrypted message: " + encrypted_message)

        decrypted_message = input("\n\nDecrypt this message. [Caesar Cipher]\n-> ")

        if decrypted_message == original_message:
            print("Correct!" +
                  "\n*******************************************************************")

        else:
            print("Hmm, something is wrong. Try again." +
                  "\n*******************************************************************")
            new_level(original_message, encrypted_message)

    
    new_level("This is a top-secret message", "Uijt jt b upq-tfdsfu nfttbhf") # level One
    #new_level(",", ",") # level Two
