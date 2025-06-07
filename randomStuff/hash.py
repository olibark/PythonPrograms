import hashlib

def get_sha256_hash(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('ASCII'))
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    input_string = input("Enter a string to hash: ")
    print(f"SHA-256 hash of '{input_string}': {get_sha256_hash(input_string)}")