import hashlib

flag = 0

pass_hash = input('Enter md5 hash: ')

wordlist = input("Enter file name: ")

try:
    pass_file = open(wordlist, 'r')
except:
    print("No such file")
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    if digest == pass_hash:
        print ('password has been found')
        print ('password is: ' + word)
        flag = 1
        break


if flag == 0:
    print ('password not in the list') 