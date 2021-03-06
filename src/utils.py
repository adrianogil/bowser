from random import randint

# Debug print
debug_mode = True
def dprint(msg):
    if debug_mode:
        print("Debug: " + msg)

def capitalize(s):
    return s[0].upper() + s[1:]

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    return False


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
 
    return False

def get_random(l):
    '''
        list l
    '''
    return l[randint(0, len(l)-1)]