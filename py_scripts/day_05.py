import hashlib

def make_string(letter_list):
    rval = ""
    for l in letter_list:
        rval += l
    return rval

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def hash(str_in):
    return hashlib.md5(str_in.encode('utf-8')).hexdigest()

def password_generator(password_id):
    counter = 1
    while(True):
        new_hash = hash(password_id + str(counter))
        if new_hash[:5] == "00000":
            yield new_hash[5], new_hash[6]
        counter += 1

def get_password(id):
    password = ""
    generator = password_generator(id)
    for _ in range(8):
        password += next(generator)[0]
    return password

def get_sophisticated_password(id):
    password_pos = {}
    generator = password_generator(id)
    while(True):
        pos, key = next(generator)
        if is_int(pos) and 0<=int(pos)<=7 and pos not in password_pos:
            password_pos[pos] = key
            if len(password_pos.keys()) == 8:
                break
    return make_string([password_pos[str(x)] for x in range(8)])

if __name__ == "__main__":
    id = "wtnhxymk"

    print(get_password(id))
    print(get_sophisticated_password(id))
