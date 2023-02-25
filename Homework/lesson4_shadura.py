# task1

print('This program is for saving and outputting notes\n'   
      'Key-words for operation the program:\n'
      'add - add note,\n'
      'earliest - out notes (from oldest to newest),\n'
      'latest - out notes (from newest to oldest),\n'
      'longest - out notes (from longest to shortest),\n'
      'shortest - out notes (from shortest to longest),\n'
      'exit - exit from the program\n')

key_word = ''
note_list = []
list_not_empty = False
note_count = 1

def print_note(list):                                       # function for output notes
    if list_not_empty:
        for i in list:
            print(i)
    else:
        print('Note list is empty! Please add any notes.')

while True:
    key_word = input('Enter key word: ')
    if key_word == 'add':                                   # input notes
        note = input('Enter note {}:'.format(note_count))
        note_list.append(note)
        list_not_empty = True
        note_count += 1
    elif key_word == 'earliest':                            # output notes from oldest to newest
        print_note(note_list)
    elif key_word == 'latest':                              # output notes from newest to oldest
        revers_note_list = note_list.copy()
        revers_note_list.reverse()
        print_note(revers_note_list)
    elif key_word == 'longest':                             # output notes from longest to shortest
        longest_note_list = note_list.copy()
        longest_note_list.sort(key=len)
        longest_note_list.reverse()
        print_note(longest_note_list)
    elif key_word == 'shortest':                            # output notes from shortest to longest
        shortest_note_list = note_list.copy()
        shortest_note_list.sort(key=len)
        print_note(shortest_note_list)
    else:
        if key_word == 'exit':                              # exit from the program
            break
        else:
            print('Incorrect kay! Don`t warry. Try again')  # Output warning about invalid input (key-words)
