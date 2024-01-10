from eth_account import Account
import secrets, string
from pprint import pprint

def desencriptInfo(encrypted, password):
    private_key = Account.decrypt(encrypted, password)
    print("DESENCRIPTANDO LA INFORMACION CON EL OBJETO Y LA CONTRASEÑA\n")
    print(f"CLAVE DESENCRIPTADA, ESTA ES LA LLAVE PIRVADA: {private_key.hex()}")

def createUserWallet():

    # 1- Crear informacion (str) random para crear llaves publica y privada de ethereum
    random = secrets.token_hex(32)
    # 2- Creando la contraseña random
    alphabet = string.ascii_letters + string.digits 
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    # 3- Crear cuenta de ethereum 
    # account.address   public key
    # account.key       private key
    account = Account.create(random)
    # 4- Encriptar la llave privada con methodo encrypt
    encripted_key = Account.encrypt(private_key=account.key, password=password)

    print("CREANDO LA CUENTA DE Ethereum Y ENCRIPTANDOLA\n")
    print(f"cuenta de ethereum: {account.address}\n")
    print(f"contraseña para encryiptar: {password}\n")
    print(f"Clave privada: {account.key.hex()}\n")
    print(f"Clave privada encriptada (objeto): {pprint(encripted_key)}")
    desencriptInfo(encripted_key, password)

createUserWallet()

# RESULTADO :

    # (createEthereumWallet) sparrow@LAPTOP-CM1N29F4:~/practicas/createEthereumWallet$ python walletCreation.py
    # CREANDO LA CUENTA DE Ethereum Y ENCRIPTANDOLA

    # cuenta de ethereum: 0x1EE6BDE51AA7e4822b7194686Ee0EED3591bF251

    # contraseña para encryiptar: enYTaKGg7a0jo40v69iy

    # Clave privada: 0x75ccdab6a75e327ce5f060157d5e1da80a024bbf1e7a6234287e77b80a24f7c1

    # {'address': '1EE6BDE51AA7e4822b7194686Ee0EED3591bF251',
    #  'crypto': {'cipher': 'aes-128-ctr',
    #             'cipherparams': {'iv': '85557e95ae219a42f943fa3681b89b6d'},
    #             'ciphertext': '1e6b27995a58562e3c56d0fdb6d97be3e26fe5c5af02f25d850a8637232aa0c8',
    #             'kdf': 'scrypt',
    #             'kdfparams': {'dklen': 32,
    #                           'n': 262144,
    #                           'p': 1,
    #                           'r': 8,
    #                           'salt': '5144ccfb079daab3894e2a0b4cfa0a7f'},
    #             'mac': '19083d654ff1d0a6bd9c9b9a7f35d5275d000b675385b7b0b8dc49b2969a354c'},
    #  'id': '30cab0d3-71cb-4bd3-b364-13fc45b9410c',
    #  'version': 3}
    # Clave privada encriptada (objeto): None
    # DESENCRIPTANDO LA INFORMACION CON EL OBJETO Y LA CONTRASEÑA

# CLAVE DESENCRIPTADA, ESTA ES LA LLAVE PIRVADA: 0x75ccdab6a75e327ce5f060157d5e1da80a024bbf1e7a6234287e77b80a24f7c1