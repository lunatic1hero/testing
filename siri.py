def unicode_to_binary(filename):
    # Read the content of the file
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check if there are at least two different characters to map to 0 and 1
    unique_chars = list(set(content))
    if len(unique_chars) < 2:
        raise ValueError("The file does not contain at least two unique characters for mapping.")

    # Assign '0' to the first character and '1' to the second
    char_to_binary = {unique_chars[0]: '0', unique_chars[1]: '1'}
    print(f"Mapping: {unique_chars[0]} -> 0, {unique_chars[1]} -> 1")

    # Convert the content to a binary string using the mapping
    binary_str = ''.join(char_to_binary[char] for char in content if char in char_to_binary)

    # Split the binary string into groups of 8 bits (1 byte each)
    byte_chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

    # Convert each byte to an ASCII character
    ascii_chars = [chr(int(byte, 2)) for byte in byte_chunks if len(byte) == 8]

    # Join the characters to form the final decoded message
    decoded_message = ''.join(ascii_chars)

    return decoded_message

# Example usage
file_path = 'Stego100-2.txt' # Replace with your actual file path
decoded_message = unicode_to_binary(file_path)
print("Decoded message:", decoded_message)
