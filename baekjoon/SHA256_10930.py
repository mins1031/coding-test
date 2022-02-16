import hashlib

n = str(input())
hash_256 = hashlib.sha256(n.encode())
print(hash_256.hexdigest())