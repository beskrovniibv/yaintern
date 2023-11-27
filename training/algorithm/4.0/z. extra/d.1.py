from string import ascii_lowercase

abc = ascii_lowercase


def encrypt(string: str, salt: int) -> str:
    result = []
    length = len(abc)
    for char in string:
        if char in abc:
            encrypted_char = abc[(ord(char) - ord(abc[0]) + salt) % length]
            result.append(encrypted_char)
        else:
            result.append(char)
    return ''.join(result)


if __name__ == '__main__':
    a = 'Hello, World!'.lower()
    print(encrypt(a, 26))
