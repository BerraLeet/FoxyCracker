# FoxyCracker
![Foxy-Cracker](https://github.com/BerraLeet/md5_crypt-hashcracker-python/assets/86689476/5f6b06e4-f355-4581-8b6a-8bee6c697932)
# MD5-Crypt Cracker Script

## Table of Contents
- [MD5-Crypt Cracker Script](#md5-crypt-cracker-script)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Disclaimer](#disclaimer)
  - [Dependencies](#dependencies)
  - [Example Usage](#example-usage)



## Description
This Python script utilizes the `passlib.hash` library to crack MD5-crypt hashes against a list of potential passwords. It serves as an educational tool to illustrate the process of hash cracking and the vulnerabilities of using outdated cryptographic methods like MD5. Can also be used in CTF's.

## Disclaimer
**WARNING:** MD5 is no longer considered secure for cryptographic purposes due to vulnerabilities to collision attacks. This script is intended for educational purposes only, to demonstrate cryptographic concepts and hash cracking techniques. Do not use this script for unauthorized access to information. Always go with ethical guidelines and legal requirements.

## Dependencies
- Python3
- pip3
- passlib (pip install) 

## Example Usage
To use this script, you need a MD5-crypt hash, a salt value, and a wordlist file (e.g., `rockyou.txt`). The script attempts to find the original password that was used to create the hash.
Salt is a value between 0-8 characters where 8 is default. User may need to define if not using default by setting using() parameter: salt_size=int number

Here's how to run the script:

```python
from passlib.hash import md5_crypt

# Define the salt and the full hash (with MD5 identifier)
salt = "dlPL2MqE"
full_hash = "$1$dlPL2MqE$oQmn16q49SqdmhenQuNgs1"

def md5_crypt_cracker(hash_to_crack, salt):
    try:
        with open("rockyou.txt", "r", encoding="latin-1") as wordlist:
            for password in wordlist:
                password = password.strip()
                if md5_crypt.using(salt=salt).hash(password) == hash_to_crack:
                    print(f"Password found: {password}")
                    return password
    except FileNotFoundError:
        print("\nWordlist file not found.")
    except KeyboardInterrupt:
        print("\nQuitting Program...Have a nice day!")
    print("Password not found.")
    return None

md5_crypt_cracker(full_hash, salt)
