import text

def main_menu():
    print(text.main_menu[0])
    for i in range(len(text.main_menu)):
        if i:
            print(f'{i:>3}. {text.main_menu[i]}')
    while True:
        choice = input(text.input_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return choice
        print(text.input_main_menu_error)


def print_message(msg: str):
    print('\n' )
    print(msg)
    print('\n')

def show_notes(book: dict, msg: str):
    if book:
        max_size = [len(max(field, key=len)) for field in zip(*list(book.values()))]
        print('\n' + '*'* (sum(max_size)+10))
        for u_id, note in book.items():
            note_str = '   '.join([f'{note[i]:<{max_size[i]}}' for i in range(len(note))])
            print(f'{u_id:>3} {note_str}')
        print('*' * (sum(max_size)+10) + '\n')
    else:
        print_message(msg)

def input_new_note(msg: list) -> list[str, str]:
    new_note = []
    for field in msg:
        new_note.append(input(field))
    return new_note

def input_info(msg: str):
    return input(msg)