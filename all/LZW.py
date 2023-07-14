def Dictionary():
    # initialize the dictionary
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    return dict_size, dictionary


# LZW encoding algorithm
def lzw_encoding(data):

    dict_size, dictionary = Dictionary()  # Getting the dictionary & dict_size

    # initialize the variables
    result = []
    unmatched = ""

    # loop through the string of data
    for character in data:

        uc = unmatched + character

        if uc in dictionary:
            unmatched = uc

        else:
            result.append(dictionary[unmatched])
            dictionary[uc] = dict_size
            dict_size += 1
            unmatched = character

    # output the code for w
    if unmatched:
        result.append(dictionary[unmatched])

    return result


def lzw_decoding(encoded_data):

    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    s = ''
    result = ''

    for code in encoded_data:

        if code not in dictionary:
            entry = dictionary[s] + dictionary[s][0]
        else:
            entry = dictionary[code]

        result = result + entry

        dictionary[code] = dictionary[s] + entry[0]
    return result


# s = "ababbabcababba"
s = "ratatatatbabratbatbabrat"
print(lzw_encoding(s))

decoded = lzw_decoding(lzw_encoding(s))
print(decoded)

if s == decoded:
    print("Success")
else:
    print("Fail")
