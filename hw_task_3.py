# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1


# with open('1.txt') as file_1:
#     content_1 = file_1.readlines()
#     print(len(content_1))

# with open('2.txt') as file_2:
#     content_2 = file_2.readlines()
#     print(len(content_2))

# with open('3.txt') as file_3:
#     content_3 = file_3.readlines()
#     print(len(content_3))

# if content_1 > content_2 and content_1 > content_3:
#     pass

with(open('1.txt') as file_1, open('2.txt') as file_2, 
open('3.txt') as file_3, open('4.txt', 'a') as file_4):
    content_1 = file_1.readlines()
    content_2 = file_2.readlines()
    content_3 = file_3.readlines()
    if len(content_1) > len(content_2) and len(content_1) > len(content_3):
        for line in file_1:
            pass


