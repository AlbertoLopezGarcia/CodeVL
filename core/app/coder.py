ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_char(c, offset): 
    # Find the index of the character in the alphabet
    index = ALPHABET.find(c)

    # Flip the index
    index = (index + 13) % 26

    # Add the offset to the index
    index += offset

    # If the index is greater than 25, wrap it around
    if index > 25:
        index -= 26

    # Return the encoded character
    return ALPHABET[index]


def encode(string):

    # Encode the string using VLCode
    encoded_str = ""
    pos = 1
    for c in string:

        # If the character is a space, reset the position
        if c == ' ':
            encoded_str += ' '
            pos = 1
            continue

        # If the character is a letter, encode it
        c = c.upper()
        encoded_str += encode_char(c, pos)
        pos += 1
        
    # Return the encoded string
    return encoded_str


def decode_char(c, offset):

    # Find the index of the character in the alphabet
    index = ALPHABET.find(c)

    # Subtract the offset from the index
    index -= offset

    # If the index is less than 0, wrap it around
    if index < 0:
        index += 26

    # Flip the index
    index = (index - 13) % 26

    # Return the decoded character
    return ALPHABET[index]


def decode(string):
    
        # Decode the string using VLCode
        decoded_str = ""
        pos = 1
        for c in string:
    
            # If the character is a space, reset the position
            if c == ' ':
                decoded_str += ' '
                pos = 1
                continue
    
            # If the character is a letter, decode it
            c = c.upper()
            decoded_str += decode_char(c, pos)
            pos += 1
            
        # Return the decoded string
        return decoded_str


if __name__ == "__main__":

    string = ""
    while (string != "quit"):

        # Get the string to encode
        string = input("Enter the string to decode: ")

        # Encode the string
        decoded_str = decode(string)
        # Print the encoded string
        print(decoded_str)