import hashlib
import sys

def md5checksum(fname): 
    md5 = hashlib.md5()
    f = open(fname, 'rb')
    while chunk := f.read(4096):
        md5.update(chunk)

    return md5.hexdigest()

def sha256checksum(fname): 
    sha256 = hashlib.sha256()

    f = open(fname, 'rb')
    while chunk := f.read(4096):
        sha256.update(chunk)

    return sha256.hexdigest()





def sha256match(result):
    if result == sys.argv[3]:
        return True
    else:
        return False
    
def md5match(result):
    if result == sys.argv[3]:
        return True
    else:
        return False
    
def hashtype():
    if sys.argv[2] == 'sha256':
        print(sha256match(sha256checksum(sys.argv[1])))
    if sys.argv[2] == 'md5':
        print(md5match(md5checksum(sys.argv[1])))

r = hashtype()
