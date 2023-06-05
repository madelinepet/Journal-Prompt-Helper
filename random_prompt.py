import random
from sys import exit, argv
import easygui


def controller(options) -> None:
    """Runs the relevant functions for user input, quitting, etc."""
    already_generated = []
    archive_answer = 'yes' if 'archive' in options else 'no'
    if 'freewrite' in options:
        prompt = 'Freewrite here'
        handle_write(None, None, prompt, None)
    current_line, prompt = generate_prompt(already_generated, archive_answer)
    already_generated.append(current_line)
    question = '\nDo you want to write about this? '
    choices = ['yes', 'y', 'no', 'n']
    answer = handle_input_capture(question, choices)
    while answer in ('n', 'no'):
        current_line, prompt = generate_prompt(
            already_generated, archive_answer)
        already_generated.append(current_line)
        answer = handle_input_capture(question, choices)
    handle_write(archive_answer, current_line, prompt, choices)


def generate_prompt(already_generated: list, archive_answer: str) -> tuple:
    """Handles generating a prompt given user input"""
    to_open = ''
    if archive_answer in ('no', 'n'):
        to_open = 'prompt_list.txt'
    else:
        to_open = 'done_or_to_revisit.txt'
    with open(to_open, "r") as f:
        content = f.readlines()
        if len(content) == len(already_generated):
            handle_full_circle()
        random_int = random.randint(0, len(content) - 1)
        while random_int in already_generated:
            random_int = random.randint(0, len(content) - 1)
        print('\n*************************')
        prompt = content[random_int].strip()
        if not len(already_generated):
            print('Your prompt is: ', '\n' + prompt)
        else:
            print('Your new prompt is: ', '\n' + prompt)
    print('*************************')
    return(random_int, prompt)


def handle_input_capture(question: str, choices: list) -> str:
    """Handles making sure the user enters recognized answers."""
    while True:
        print(question)
        answer = input('--> ').lower().strip()
        if answer in (choices):
            break
        else:
            ask = '\n***Please enter one of the following: '
            print(ask + ', '.join(choices) + '.***')
    return answer


def handle_full_circle() -> None:
    """Handles the case where a user circles through all of their prompts"""
    print('\n*************************')
    print('You circled through all of your prompts!')
    question = """Type "1" to revisit something from your archive,
     "2" to freewrite about your day,
     "3" to start over from your active list, or
     "4" to quit.
    """
    ds = {
        '1': ['archive'],
        '2': ['freewrite'],
        '3': [''],
        '4': ['']
     }
    choices = ds.keys()
    answer = handle_input_capture(question, choices)
    if answer != '4':
        for key, value in ds.items():
            if answer == key:
                controller(value)
    else:
        message = 'See you next time!'
        handle_quit(message)


def handle_write(
    archive_answer: str,
    current_line: str,
    prompt: str,
    choices: list
        ) -> None:
    """Handles the journaling window logic"""
    message = 'No changes made to your lists.'
    if archive_answer in ('y', 'yes'):
        arch_msg = 'Your prompt was already in your archive.\n'
        message = arch_msg + message
    elif archive_answer is not None:
        delete_me_question = '\nRemove from active list and add to completed? '
        do_delete = handle_input_capture(delete_me_question, choices)
        if do_delete in ('yes', 'y'):
            move_line_to_done(current_line)
            message = 'Lists updated!'
    easygui.textbox(prompt + ' - (this will not be saved)')
    handle_quit(message)


def move_line_to_done(current_line: int) -> None:
    """Effectively moves the prompt from active list to
     their done or to revisit list"""
    new_content = ''
    with open("done_or_to_revisit.txt", "a") as dest:
        with open("prompt_list.txt", "r") as src:
            content = src.readlines()
            dest.write('\n' + content[current_line].strip())
            print('\nPrompt written to done or revisit list...')
            new_content = content
            del new_content[current_line]
    with open("prompt_list.txt", "w") as f:
        print('...And prompt removed from active list!\n')
        f.write(''.join(new_content))


def handle_quit(message: str) -> None:
    """Provides messaging around quitting the script."""
    print('\n*************************')
    print(message)
    reminder = generate_random_reminder()
    print('Remember: \n' + reminder)
    print('Quitting...')
    print('Thank you for using this prompt generator.')
    print('*************************\n')
    exit(0)


def generate_random_reminder() -> str:
    """Generates a random reminder from your truths file."""
    with open('reminders.txt', "r") as f:
        content = f.readlines()
        random_int = random.randint(0, len(content) - 1)
        return '***' + content[random_int].strip() + '***'


if __name__ == '__main__':
    """Highest level controller for freewrite vs prompt modes."""
    print(' -----------------------------------------')
    print('| Welcome to the random prompt generator! |')
    print(' -----------------------------------------')
    try:
        controller(argv)
    except KeyboardInterrupt:
        message = 'KeyboardInterrupt detected'
        handle_quit(message)
