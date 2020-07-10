import base64


# Lara Argento
# Convert a PDF file to base64 string. 
with open("arquivoPDF.pdf", "rb") as pdf_file:
    encoded_bytes = base64.b64encode(pdf_file.read())
    encoded_string = encoded_bytes.decode('utf-8')
    #print(encoded_string)

# This overwrites the text on the file.
f = open("base64string.txt", "w")
f.write(encoded_string)
f.close()