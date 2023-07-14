def encoded(input_file, output_file):
    with open(input_file,'r') as file_in, open(output_file,'w') as file_out:
        dictionary = {chr(i) : i for i in range(256)}
        next_code = 256
        data = file_in.read()
        current_str = ''
        encoded_str = []

        for ch in data:
            new_str = current_str + ch
            if new_str in dictionary:
                current_str = new_str
            else:
                encoded_str.append(dictionary[current_str])
                dictionary[new_str] = next_code
                next_code += 1
                current_str = ch
        encoded_str.append(dictionary[current_str])
        file_out.write(" ".join(str(code) for code in encoded_str))

def decoded(input_file,output_file):
    with open(input_file,'r') as file_in , open(output_file,'w') as file_out:
        dictionary = {i : chr(i) for i in range(256)}
        next_code = 256
        encoded_data = file_in.read().split()
        current_str = dictionary[int(encoded_data[0])]
        decoded_data = current_str

        for code in encoded_data[1:]:
            if int(code) in dictionary:
                new_str = dictionary[int(code)]
            decoded_data += new_str
            dictionary[next_code] = current_str + new_str[0]
            next_code +=1
            current_str = new_str
        file_out.write(decoded_data)


input_file_path = "input.txt"
encoded_file_path = "encoded.txt"
decoded_file_path = "decoded.txt"

encode = encoded(input_file_path, encoded_file_path)
decode = decoded(encoded_file_path,decoded_file_path)