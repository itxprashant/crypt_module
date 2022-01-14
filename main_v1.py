alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZab1cd3e2f4ghi5jkl6mn7opq8rs9 t0uvwxyz"
fu = open("key_example","r")
mykey = fu.read()


def create_key(key_text):
    pass
    
def encrypt(text, key):

    xkey = key
    pairs_enc = {alphabets[i]: xkey[i] for i in range(len(alphabets))}
    enc_text = str()
    for i in range(len(text)):        
        enc_text += pairs_enc[text[i]]
 

    return enc_text




def decrypt(text, key):

    xkey = key
    pairs_dec = {alphabets[i]: xkey[i] for i in range(len(alphabets))}
    dec_text = str()
    for i in range(len(text)):        
        dec_text += pairs_enc[text[i]]
 

    return dec_text
fu.close()