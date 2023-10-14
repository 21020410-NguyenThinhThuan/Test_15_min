#
# Mã hóa tên sinh viên
#

def newascii(ch):
	ascii_value = ord(ch) + 100;
	return ascii_value;

def oldascii(ascii_val):
	old_ascii = int(ascii_val) - 100;
	return old_ascii;


string = ''

def encode(msg):
	string_ascii = ''
	for i in msg:
		string_ascii+=str(newascii(i));

	return string_ascii;

def decode(newascii_string):
	pack = ''
	i = 0
	dec_message = ''
	while (i < len(str(newascii_string))):
		
		pack = newascii_string[i:i+3]
		dec_message+=chr(oldascii(pack))
		i=i+3

	return dec_message;	

def encode_1(msg):
    binary_string = ''
    for char in msg:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:]  
        binary_string += binary_value
    return binary_string

def decode_1(binary_string):
    decoded_message = ''
    i = 0
    while i < len(binary_string):
        binary_char = binary_string[i:i+8]  
        ascii_value = int(binary_char, 2)  
        decoded_char = chr(ascii_value)
        decoded_message += decoded_char
        i += 8
    return decoded_message

msg = input("Enter the message: ")
encoded_string = encode(msg)
print("Encoded string: ", encoded_string)
decoded_string = decode(encoded_string)
print("Decoded string: ", decoded_string)
encoded_string_1 = encode_1(msg)
print("Encoded string: ", encoded_string_1)
decoded_string_1 = decode_1(encoded_string_1)
print("Decoded string: ", decoded_string)