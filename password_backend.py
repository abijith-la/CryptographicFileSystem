from passlib.hash import pbkdf2_sha256

def password_backend(password):
    f = open("hashDO_NOT_DELETE.txt",'r+')
    existpass = f.read()
    return pbkdf2_sha256.verify(password, existpass)
