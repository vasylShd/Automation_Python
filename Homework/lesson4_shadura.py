# task1

print('This program use for saving and outputting notes\n'
      'Key-words for operation of the program:\n'
      'add - add note,\n'
      'earliest - output notes (from oldest to newest),\n'
      'latest - output notes (from newest to oldest),\n'
      'longest - output notes (from longest to shortest),\n'
      'shortest - output notes (from shortest to longest),\n'
      'exit - exit from the program\n')

key_word = ''
note_list = []
list_not_empty = False
note_count = 1

def print_note(list):                                   # function for output notes
    if list_not_empty:
        for i in list:
            print(i)
    else:
        print('¯\_(ツ)_/¯ Note list is empty! Please add any note.')

while True:
    key_word = input('Enter key word: ')
    if key_word == 'add':                               # input notes
        note = input('Enter note {}:'.format(note_count))
        if note == '':                                  # Output warning if the note is empty
            print('¯\_(ツ)_/¯ Note cannot be empty! Try again.')
        else:
            note_list.append(note)
            list_not_empty = True
            note_count += 1
    elif key_word == 'earliest':                        # output notes from oldest to newest
        print_note(note_list)
    elif key_word == 'latest':                          # output notes from newest to oldest
        revers_note_list = note_list.copy()
        revers_note_list.reverse()
        print_note(revers_note_list)
    elif key_word == 'longest':                         # output notes from longest to shortest
        longest_note_list = note_list.copy()
        longest_note_list.sort(key=len)
        longest_note_list.reverse()
        print_note(longest_note_list)
    elif key_word == 'shortest':                         # output notes from shortest to longest
        shortest_note_list = note_list.copy()
        shortest_note_list.sort(key=len)
        print_note(shortest_note_list)
    else:
        if key_word == 'exit':                           # exit from the program
            print('Goodbye! (・_・)ノ')
            break
        elif key_word == '':                             # Output warning about invalid input (key-words)
            print('¯\_(ツ)_/¯ Key cannot be empty! Enter correct key.')
        else:
            print('¯\_(ツ)_/¯ Incorrect key! Don`t warry. Try again.')
