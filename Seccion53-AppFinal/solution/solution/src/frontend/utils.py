

def input_valid_int(msg, start = 0, end = None):
    # keep iterating till the given input is valid
    # hidden assumption: both start and end either value or none. That is bad
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
                # another way is to check if int(inp) in range(start, end+1)
            else:
                return int(inp)
        else:
            return int(inp)


def get_menu_choice(top_msg, messages):
    print(f'\n{top_msg}')

    messages = [f'{idx+1}) {msg}' for idx, msg in enumerate(messages)]
    print('\n'.join(messages))

    msg = f'Enter your choice (from 1 to {len(messages)}): '
    return input_valid_int(msg, 1, len(messages))