import rsa
import util.util as util

def generate_rsa_key(bits):
    # Generate an RSA key pair with the specified number of bits
    (pubKey,privkey) = rsa.newkeys(bits)

    # Convert the private key components to long integers
    n = privkey.n
    publicKey = privkey.e
    privateKey = privkey.d
    
    integerForMessage = util.stringToInteger("Yellow")
    ciphertext = pow(integerForMessage,publicKey,n)
    print(ciphertext)

    plaintext = util.integerToString(pow(ciphertext,privateKey,n))
    print(plaintext)

generate_rsa_key(2048)