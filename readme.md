# Ethereum Wallet Creation and Encryption

This Python script (`walletCreation.py`) demonstrates the creation of an Ethereum wallet and the encryption of its private key using the `eth_account` library. It generates a random Ethereum account, creates a password for encryption, and then encrypts the private key. Additionally, it provides a decryption function to retrieve the original private key.

## Prerequisites

Make sure you have Python installed on your system. You can install the required dependencies using the following command:
```bash
pip install eth_account
```

## How to Use?
Clone this repository to your local machine:
```bash
git clone https://github.com/Alberto200420/createEthereumWallet
```
## Navigate to the project directory:
```bash
cd createEthereumWallet
```
## Run the Python script:

```bash
python walletCreation.py
```
## Output
Upon running the script, you will see output similar to the following:

```bash
CREATING Ethereum WALLET AND ENCRYPTING IT

Ethereum account: 0x1EE6BDE51AA7e4822b7194686Ee0EED3591bF251

Encryption password: enYTaKGg7a0jo40v69iy

Private key: 0x75ccdab6a75e327ce5f060157d5e1da80a024bbf1e7a6234287e77b80a24f7c1

{
 'address': '1EE6BDE51AA7e4822b7194686Ee0EED3591bF251',
 'crypto': {
   'cipher': 'aes-128-ctr',
   'cipherparams': {'iv': '85557e95ae219a42f943fa3681b89b6d'},
   'ciphertext': '1e6b27995a58562e3c56d0fdb6d97be3e26fe5c5af02f25d850a8637232aa0c8',
   'kdf': 'scrypt',
   'kdfparams': {'dklen': 32, 'n': 262144, 'p': 1, 'r': 8, 'salt': '5144ccfb079daab3894e2a0b4cfa0a7f'},
   'mac': '19083d654ff1d0a6bd9c9b9a7f35d5275d000b675385b7b0b8dc49b2969a354c'},
 'id': '30cab0d3-71cb-4bd3-b364-13fc45b9410c',
 'version': 3
}
Encrypted private key (object): None

DECRYPTING INFORMATION WITH THE OBJECT AND PASSWORD

DECRYPTED PRIVATE KEY: 0x75ccdab6a75e327ce5f060157d5e1da80a024bbf1e7a6234287e77b80a24f7c1
```

License
This project is licensed under the MIT License - see the LICENSE.md file for details.