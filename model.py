from copy import deepcopy

class Notes:
    def __init__(self, path: str = 'notes.txt'):
        self.notes = {}
        self.original_notes = {}
        self.path = path

    def open_file(self):
        with open(self.path, 'r', encoding = 'UTF-8') as file:
            note_lines = file.readlines()
        for u_id, note_line in enumerate(note_lines, 1):
            note_line = note_line.strip().split(';')
            self.notes[u_id] = note_line
        self.original_notes = deepcopy(self.notes)

    def save_file(self):
        note_lines = [';'.join(note_line) for note_line in self.notes.values()]
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(note_lines))
        
        

    def next_id(self):
        return max(self.notes)+1

    def new_note(self, note_line: list):
        self.notes[self.next_id()] = note_line

    def search(self, word: str) -> dict[int, list[str, str]]:
        result = {}
        for u_id, note_line in self.notes.items():
            if word.lower() in ''.join(note_line).lower():
                result[u_id] = note_line
        return result

    def edit(self, u_id: int, note_line: list[str, str]) -> str:
        old_note = self.notes.get(u_id)
        new_note = [note_line[i] if note_line[i] else old_note[i] for i in range(len(note_line))]
        self.notes[u_id] = new_note
        return new_note[0]

    def delete(self, u_id: int) -> str:
        return self.notes.pop(u_id)[0]
