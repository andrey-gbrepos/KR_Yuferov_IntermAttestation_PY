import text
import view
from model import Notes



def start():
    nt = Notes()
    while True:
        choice = view.main_menu()
        match choice:
            case '1':
                nt.open_file()
                view.print_message(text.open_successful)
            case '2':
                view.show_notes(nt.notes, text.empty_notes_error)
            case '3':
                note_line = view.input_new_note(text.input_new_note)
                nt.new_note(note_line)
                view.print_message(text.note_successful_result(note_line[0], 0))
            case '4':
                nt.save_file()
                view.print_message(text.save_successful)
            
            case '5':
                    u_id = view.input_info(text.input_edit_id)
                    new_note = view.input_new_note(text.input_edit_note)
                    name = nt.edit(int(u_id), new_note)
                    view.print_message(text.note_successful_result(name, 1))
            case '6':
                    u_id = view.input_info(text.input_delete_id)
                    confirm_note = nt.notes.get(int(u_id))[0]
                    if view.input_info(text.confirm_delete_note(confirm_note)).lower() == 'y':
                        name = nt.delete(int(u_id))
                        view.print_message(text.note_successful_result(name, 2))
            case '7':
                if nt.original_notes != nt.notes:
                    if view.input_info(text.confirm_changes).lower() == 'y':
                        nt.save_file()
                view.print_message(text.good_bay)
                break