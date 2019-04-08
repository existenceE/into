
from PIL import Image
import tesserocr




# # image = Image.open('imagetest.png')
# image = Image.open('code2.png')
# result = tesserocr.image_to_text(image)
# print(result)
#
#
# # print(tesserocr.file_to_text('code.jpg'))


image = Image.open('code2.png')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
image.show()
print(result)








































