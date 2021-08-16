import easyocr
reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext('img.png')

print(result)
print("-------------------------------------------------------------------------------------------------------------------")
for array in result:
    key = array[0]
    word = array[1]
    print(word)

print("-------------------------------------------------------------------------------------------------------------------")
