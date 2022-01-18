import random
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{]};:\'\"\\,./<>?"


class Cryptography:
    @classmethod
    def read_key(self):
        fu = open("key","r")
        mykey = fu.read()
        fu.close()
        return mykey
    @classmethod
    def create_key(self):
        fu = open("key", "w")
        fu.write(''.join(random.sample(alphabets,len(alphabets))))
        fu.close()
    @classmethod
    def encrypt(self,text, key):
        xkey = key
        pairs_enc = {alphabets[i]: xkey[i] for i in range(len(alphabets))}
        enc_text = str()
        for i in range(len(text)):
            enc_text += pairs_enc[text[i]]
        return enc_text
    @classmethod
    def decrypt(self,text, key):
        xkey = key
        pairs_dec = {xkey[i]: alphabets[i] for i in range(len(alphabets))}
        dec_text = str()
        for i in range(len(text)):
            dec_text += pairs_dec[text[i]]
        return dec_text
