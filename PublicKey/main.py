from Encryption import *
from Decryption import *

#Job 3:2
bibleVerse = "He said"
decryption = Decryption()
encryption = Encryption(decryption.GeneratePublicKey())

cipherText = encryption.EncryptText(bibleVerse)
plainText = decryption.DecryptText(cipherText)

print(cipherText)
print(plainText)
