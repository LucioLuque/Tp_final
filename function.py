from notes import notes_mapping

def function(note):
    for tuple in notes_mapping:
        if note == tuple[0]:
            return tuple[1]

