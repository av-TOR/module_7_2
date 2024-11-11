f_name = "str.txt"


def custom_write(file_name, strings):
    num_str = 0
    strings_positions = {}

    file = open(file_name, 'a+', encoding="utf-8")

    for i in strings:
        num_str += 1
        key = (num_str, file.tell())
        file.write(f"{i}\n")
        strings_positions[key] = i

    file.close()

    return strings_positions

new_str = ["Srtings or number?", "Что будет, если...",
           "Молекулярный разбор объекта - мир глазами химика или физика?", "Кошка вам не собака"]

res = custom_write('str.txt', new_str)
for i in res.items():
    print(i)