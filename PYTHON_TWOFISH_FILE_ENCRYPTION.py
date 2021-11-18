from twofish import Twofish

def fencrypt(infile, outfile, password):
    bs  = 16 #16 bytes or 128 bits block size
    plaintext = infile.read() 
    
    if len(plaintext) % bs: #padding the plaintext before encryption
        padding_length = (bs - len(plaintext) % bs) or bs
        plaintext += str.encode(padding_length * chr(padding_length))
        padded_plaintext = plaintext
    else:
        padded_plaintext = str.encode(plaintext)
    
    T = Twofish(str.encode(password)) #our cipher

    for x in range(int(len(padded_plaintext)/bs)):
        chunk = padded_plaintext[x*bs:(x+1)*bs]
        outfile.write(T.encrypt(chunk)) #write ciphertext to file on disk

def fdecrypt(infile, outfile, password):
    bs  = 16 #16 bytes or 128 bits block size
    cipherText = infile.read() 

    T = Twofish(str.encode(password)) #our cipher

    next_chunk = ''

    for x in range(int(len(cipherText)/bs)): #read encrypted chunks from disk
        chunk, next_chunk = next_chunk, T.decrypt(cipherText[x*bs:(x+1)*bs])
        outfile.write(bytes(x for x in chunk))

password = '12345'

with open('infile.txt', 'rb') as infile, open('outfile.txt', 'wb') as outfile:
    fencrypt(infile, outfile, password)

with open('outfile.txt', 'rb') as infile, open('outfile_decrypted.txt', 'wb') as outfile:
    fdecrypt(infile, outfile, password)




