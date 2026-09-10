
import bcrypt


def hashStr(str_raw: str) -> str:
    """
    Hash a String.
    """
    str_byte = str_raw.encode('utf-8')
    salt_hash = bcrypt.gensalt()
    hash_byte = bcrypt.hashpw(str_byte, salt_hash)
    return hash_byte.decode('utf-8')
    
def compareHash(str_raw: str, str_hash: str) -> bool:
    """
    Return True if the string match the hash.
    """
    str_byte = str_raw.encode('utf-8')
    hash_byte = str_hash.encode('utf-8')
    return bcrypt.checkpw(str_byte, hash_byte)