def lzw_encode(data):
    # Initialize dictionary with single-character codes
    dictionary = {chr(i): i for i in range(256)}
    # print(dictionary)
    dictionary_index = 256  # Next available code for dictionary entries
    current_sequence = ""  # Current sequence of characters
    result = []  # Store the encoded data

    for char in data:
        current_sequence += char  # Add the next character to the current sequence

        if current_sequence not in dictionary:  # If the current sequence is not in the dictionary
            # Add the current sequence to the dictionary
            dictionary[current_sequence] = dictionary_index
            dictionary_index += 1  # Increment the next code

            # Append the code for the previous sequence to the result
            print(current_sequence, current_sequence[:-1])
            result.append(dictionary[current_sequence[:-1]])

            current_sequence = char  # Start a new sequence with the current character

    # Append the code for the last sequence to the result
    result.append(dictionary[current_sequence])

    return result


def lzw_decode(compressed_data):
    # Initialize dictionary with single-character codes
    dictionary = {i: chr(i) for i in range(256)}
    dictionary_index = 256  # Next available code for dictionary entries
    # Get the first code from compressed data
    current_code = compressed_data.pop(0)
    # print(current_code)

    # Initialize output with the sequence represented by current_code
    output = dictionary[current_code]

    result = [output]  # Store the decoded data

    for code in compressed_data:
        if code in dictionary:  # If the code is in the dictionary
            entry = dictionary[code]  # Get the entry for the code
        else:
            entry = dictionary[current_code] + \
                dictionary[current_code][0]  # Get the new entry
            # print("print", dictionary[current_code],
            #       dictionary[current_code][0])

        result.append(entry)  # Add entry to the result

        dictionary[dictionary_index] = dictionary[current_code] + \
            entry[0]  # Add new entry to the dictionary

        dictionary_index += 1  # Increment the next code

        current_code = code  # Update the current code

    return ''.join(result)


# Example usage:

data = "ratatatatbabratbatbabrat"  # Example input data
# data = "ababbabcababba"
# data = "1122233333332222121"
encoded_data = lzw_encode(data)
print("Encoded data:", encoded_data)

decoded_data = lzw_decode(encoded_data)
print("Decoded data:", decoded_data)

if data == decoded_data:
    print("Success")
else:
    print("Fail")
