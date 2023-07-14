# Run length encoding--- compresses a string of characters
# by replacing repeated characters with the character followed
# by the number of repetitions. For example, the string
# "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# The string "AAB" would be encoded as "2A1B".
# The string "A" would be encoded as "1A".
# The empty string would be encoded as "".

def Encode(s):
    if len(s) == 0:
        return ""
    else:
        count = 1
        prev = s[0]
        result = ""
        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                result += str(count) + prev
                count = 1
                prev = s[i]
        result += str(count) + prev
        return result


def Decode(s):
    if len(s) == 0:
        return ""
    else:
        count = 0
        result = ""
        for i in range(len(s)):
            if s[i].isdigit():
                count = count * 10 + int(s[i])
            else:
                result += s[i] * count
                count = 0
        return result


with open("RLE_input.txt", "r") as f:
    s = ''
    for line in f:
        s = s + line

    encoded = Encode(s)

    with open("RLE_output.txt", "w") as f:
        f.write(encoded)

    decoded = Decode(encoded)
