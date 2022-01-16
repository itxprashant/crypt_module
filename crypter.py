import main_v1 as mod
print("""List of command:
g - Generate new key
i - insert new key
e - encrypt a text
d - decrypt a text.\n""")
while True:
    x = input("Enter a command:").lower()
    if x == 'g':
        mod.create_key()
        print("Generated key: ",mod.read_key()) 
    elif x == 'i':
        f = open("key","w")
        y = input("Enter a key(must be a generated one): ")
        f.write(y)
        f.close()
        print("Key added successfully!")
    elif x == 'e':
        z = input("Enter a text to encrypt: ")
        print("Encrypted text: ", mod.encrypt(z, mod.read_key()))
    elif x == 'd':
        zz = input("Enter a text to decrypt: ")
        print("Decrypted text: ", mod.decrypt(zz, mod.read_key()))