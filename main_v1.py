import random
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZab1cd3e2f4ghi5jkl6mn7opq8rs9 t0uvwxyz"



def read_key():
    fu = open("key","r")
    mykey = fu.read()
    fu.close()
    return mykey
    pass


def create_key():
    fu = open("key", "w")
    fu.write(''.join(random.sample(alphabets,len(alphabets))))
    fu.close()

def encrypt(text, key):

    xkey = key
    pairs_enc = {alphabets[i]: xkey[i] for i in range(len(alphabets))}
    enc_text = str()
    for i in range(len(text)):        
        enc_text += pairs_enc[text[i]]
 

    return enc_text




def decrypt(text, key):

    xkey = key
    pairs_dec = {xkey[i]: alphabets[i] for i in range(len(alphabets))}
    dec_text = str()
    for i in range(len(text)):        
        dec_text += pairs_dec[text[i]]
 

    return dec_text
