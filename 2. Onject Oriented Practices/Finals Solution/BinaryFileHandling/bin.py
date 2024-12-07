# # Cast bytes to bytearray
# mutable_bytes = bytearray(b'\x00\x0F')
# print(mutable_bytes)
# # Bytearray allows modification
# mutable_bytes[0] = 255
# mutable_bytes.append(255)
# print(mutable_bytes)

# # Cast bytearray back to bytes
# immutable_bytes = bytes(mutable_bytes)
# print(immutable_bytes)



# text = "Hello, World!"
# byte_data = text.encode('utf-8')
# print(byte_data)
# d=byte_data.decode('ascii')
# print(d)

original_text = "Hello, World! 🌍"  # Includes a non-ASCII character (earth emoji)
encoded_data = original_text.encode('utf-8')

try:
    decoded_text = encoded_data.decode('ascii')
    print("Decoded:", decoded_text)
except UnicodeDecodeError as e:
    print(f"Error decoding: {e}")
