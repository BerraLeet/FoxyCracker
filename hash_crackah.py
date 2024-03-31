from passlib.hash import md5_crypt

# Example usage below
# Reminder !! Full hash must contain the md5 identifier "$1$" the salt and hash example written in script
# Salt variable Requires a string of 8 characters (Default) 
salt = "dlPL2MqE"
full_hash = "$1$dlPL2MqE$oQmn16q49SqdmhenQuNgs1"
# this case using rockyou.txt, example hash with return password "hello"

def md5_crypt_cracker(hash_to_crack, salt):
    try:
        with open("rockyou.txt", "r", encoding="utf-8") as wordlist:
            for password in wordlist:
                password = password.strip()
                # calculating MD5-crypt, setting the salt with using function
                if md5_crypt.using(salt=salt).hash(password) == hash_to_crack:
                    print(f"Password found: {password}")
                    return password
    except FileNotFoundError:
        print("\nWordlist file not found.")
    except KeyboardInterrupt:
        print("\nQuitting Program...Have a nice day!")
    print("Password not found.")
    return None

# Calling function
md5_crypt_cracker(full_hash, salt)
