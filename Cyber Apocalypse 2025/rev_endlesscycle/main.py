import struct

encrypted_data = [
    0xb6, 0x9e, 0xad, 0xc5, 0x92, 0xfa, 0xdf, 0xd5,
    0xa1, 0xa8, 0xdc, 0xc7, 0xce, 0xa4, 0x8b, 0xe1,
    0x8a, 0xa2, 0xdc, 0xe1, 0x89, 0xfa, 0x9d, 0xd2,
    0x9a, 0xb7
]

xor_key = 0xBEEFCAFE

original_bytes = bytearray()
for i in range(0, len(encrypted_data), 4):
    chunk = encrypted_data[i:i+4]
    while len(chunk) < 4:
        chunk.append(0)

    encrypted_int = struct.unpack("<I", bytes(chunk))[0]
    decrypted_int = encrypted_int ^ xor_key
    original_bytes.extend(struct.pack("<I", decrypted_int))

original_input = original_bytes.rstrip(b'\x00').decode(errors="ignore")

print("Original input:", original_input)
