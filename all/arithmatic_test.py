# Arithmetic Encoding

def arithmetic_encode(data, probabilities):
    low = 0.0
    high = 1.0
    range_width = 1.0

    for symbol in data:
        symbol_range = high - low
        high = low + symbol_range * probabilities[symbol][1]
        low = low + symbol_range * probabilities[symbol][0]
        range_width = high - low

    return (low + high) / 2


# Arithmetic Decoding

def arithmetic_decode(encoded_value, probabilities, num_symbols):
    result = []
    low = 0.0
    high = 1.0
    value = encoded_value

    for x in range(num_symbols):
        for symbol, (symbol_low, symbol_high) in probabilities.items():
            symbol_range = high - low
            symbol_value = (value - low) / symbol_range

            if symbol_low <= symbol_value < symbol_high:
                result.append(symbol)
                high = low + symbol_range * symbol_high
                low = low + symbol_range * symbol_low
                break

    return result


# Example usage:
# Data to encode
# data = "ABBCCCDDDDEEEEE"
# data = "ratatatatbabratbatbabrat"
# data = '1332'
data = []
with open('input.txt', 'r') as file:
    data = file.read()

symbol_counts = {}
for symbol in data:
    symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
# print(symbol_counts)

probabilities = {}
total_symbols = len(data)
for symbol, count in symbol_counts.items():
    print(symbol, count)

    probabilities[symbol] = (sum(symbol_counts[s] for s in symbol_counts.keys() if s < symbol) / total_symbols,
                             sum(symbol_counts[s] for s in symbol_counts.keys() if s <= symbol) / total_symbols)

    # probabilities[symbol] = count / total_symbols
    print(probabilities[symbol])
# Encode the data
encoded_value = arithmetic_encode(data, probabilities)
print("Encoded value:", encoded_value)

# Decode the encoded value
decoded_data = arithmetic_decode(encoded_value, probabilities, len(data))
print("Decoded data:", ''.join(decoded_data))
