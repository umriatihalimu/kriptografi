def keys(key) :
    s = [x for x in range(256)]
    j=0
    key=[ord(x) for x in key]
    for i in range(256):
        j=(j+s[i]+int(key[i%len(key)]))%256
    return s

def encryptor(s, plaintext):
    i,j=0,0
    ciphertext=[]
    for char in plaintext:
        i=(i+j)%256
        j=(j+s[i])%256
        s[i],s[j]=s[j],s[i]
        hexed = format(ord(chr(s[(s[i]+s[j])%256] ^ ord(char))), 'x')
        ciphertext.append(hexed)
        
    return ciphertext
        
key = input ("\n masukkan key : ")
s = keys(key)
ciphertext = encryptor (s, input('\n masukkan plaintext : '))

print ("\n ciphertext adalah : ")
for x in ciphertext :
    print(x, end='')
print("\n")