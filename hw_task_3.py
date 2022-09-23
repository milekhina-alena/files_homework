with(open('1.txt') as file_1, open('2.txt') as file_2, 
open('3.txt') as file_3):
    counter_1 = 0
    for line in file_1.readlines():
        counter_1 += 1
    counter_2 = 0
    for line in file_2.readlines():
        counter_2 += 1
    counter_3 = 0
    for line in file_3.readlines():
        counter_3 += 1

text_4 = dict()
with(open('1.txt') as file_1, open('2.txt') as file_2, 
open('3.txt') as file_3):
    f_1 = file_1.read()
    content_1 = [counter_1, f_1]
    text_4['1.txt'] = content_1
    f_2 = file_2.read()
    content_2 = [counter_2, f_2]
    text_4['2.txt'] = content_2
    f_3 = file_3.read()
    content_3 = [counter_3, f_3]
    text_4['3.txt'] = content_3


max_key = max(text_4, key = lambda k: text_4[k])
min_key = min(text_4, key = lambda k: text_4[k])

with open('4.txt', 'a') as file_4:
    result_1 = min_key + '\n' + str(text_4[min_key][0]) + '\n' + text_4[min_key][1] + '\n\n'
    file_4.write(result_1)
    for key in text_4.keys():
        if key != max_key and key != min_key:
            result_2 = key + '\n' + str(text_4[key][0]) + '\n' + text_4[key][1] + '\n\n'
    file_4.write(result_2)
    result_3 = max_key + '\n' + str(text_4[max_key][0]) + '\n' + text_4[max_key][1] + '\n\n'
    file_4.write(result_3)