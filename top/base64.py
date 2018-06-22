import base64
#
# with open("arroz.jpg", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
with open("arroz.jpg", "rb") as f:
    data = f.read()
    print data.encode("base64")