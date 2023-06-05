# Journaling Random Prompt Generator
A Python script that helps you choose a random prompt from your list to journal about. Optionally removes prompts you decide to write about from your active list of topics and adds them to an archive file for you to revisit later.

For inspiration about what prompts to include, I highly recommend looking into the process described [here](https://www.thecureforchronicpain.com/journalspeak).

## Getting Started
- Clone this repository using your preferred method. 
- Add your list of prompts to the `prompt_list.txt` file. The only requirement here is that each prompt is on a different line as shown.
- Add reminders that resonate with you to the `reminders.txt` file, again making sure they're each on their own line as shown.

## Running the Script
- cd into wherever you cloned the directory in your terminal.
- Install the dependencies: `pip3 install -r requirements.txt`
- Run `python3 random_prompt.py`
- Follow the prompts.
- To load directly from your archive, run: `python3 random_prompt.py archive`
- To freewrite, run `python3 random_prompt.py freewrite`

## Future Features
- Add things to takeaways file?
- Ability to add your own prompt one day? Worth it?
- Timer
- Add wins for the day
- Refactor as react app?