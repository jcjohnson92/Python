import sys
import hashlib

file1 = sys.argv[1]

sha256 = hashlib.sha256()
md5=hashlib.md5()

def hashfile_sha256(file):
    with open(file, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            sha256.update(data)
        return sha256.hexdigest()
    
def hashfile_md5(file):
    with open(file, 'rb') as f:
            while True:
                data = f.read()
                if not data:
                    break
                md5.update(data)
            return md5.hexdigest()



file_hash_sha256 = hashfile_sha256(file1)
file_hash_md5 = hashfile_md5(file1)

print(f"sha256 Hash:{file_hash_sha256}\nMD5 HASH:{file_hash_md5}")

