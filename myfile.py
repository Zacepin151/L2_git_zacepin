def create_file_with_text(filename):
    with open(filename, 'w') as file:
        file.write("Hello, File!")

create_file_with_text('example.txt')

def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")


read_file_content('example.txt')

def append_text_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write('\n' + text)


append_text_to_file('example.txt', 'New line added!')


create_file_with_text('example.txt')


read_file_content('example.txt')

append_text_to_file('example.txt', 'New line added!')

read_file_content('example.txt')
