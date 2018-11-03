text = input('Enter Message : ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
key=3
cypher=''
for t in text:
    if t in alphabet :
        cypher += alphabet[(alphabet.index(t)+key)%(len(alphabet))]
print('Encrypted Message is : '+cypher)
