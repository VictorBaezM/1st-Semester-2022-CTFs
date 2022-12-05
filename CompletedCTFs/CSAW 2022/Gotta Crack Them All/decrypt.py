#def get_key():
#    encrypted = b'kz\xc6\xb9\xd9Du\xcb\x8a\x9e\xe0\x9d\xbeo\xee\x03\xcf\xddd'
#    plain = 'Cacturne-Grass-Dark'

#    return [ord(x)^z for (x,z) in zip(plain,encrypted)]
#Got original password by guessing last character.
def get_key():
    encrypted = b'on\xdf\xb7\xc0Yi\xca\x8a\x9d\xf3\x8e\xa61\x875\xcf\xc8`\xfb'
    plain = 'Guzzlord-Dark-Dragon'

    return [ord(x)^z for (x,z) in zip(plain,encrypted)]




with open("encrypted_passwords.txt","rb") as fd:
    data = fd.readlines()
    key = get_key()

    results = []
    for password in data:
        decrypted = ""
        for i in range(0,len(password)-1):
            if i >= len(key):
                decrypted = decrypted + chr(ord(' ')^password[i])
            else:
                decrypted = decrypted + chr(key[i]^password[i])
        results.append(decrypted)

    print(results)
    print(max(results))
