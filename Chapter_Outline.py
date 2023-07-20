from TextGen import textgen as generate_text
from TextGen import textgen3 as generate_text3

# The summary of the chapter
brief_summary = "In this chapter, the protagonist John discovers the secret society, " \
                "faces a conflict with his long-time friend, and finds an unexpected ally."

# The modified prompt
outline_prompt = (f"Generate a more detailed summary of the chapter based on the following brief summary: "
                  f"{brief_summary}. The summary should break down the main events in the chapter, "
                  f"each event should be separated by the '--evnt--' divider. Provide a detailed description "
                  f"of each event, including the characters involved, the location, any important dialogues, "
                  f"the emotional impact on the characters, and the implications for the overall plot. For example: "
                  f"\n--evnt--\nJohn's discovery of the secret society happens in an abandoned warehouse "
                  f"where he accidentally stumbles upon a secret meeting. The shock and fear he feels are palpable "
                  f"as he realizes the depth of the conspiracy he has uncovered."
                  f"\nThe total outline should be ")
print(outline_prompt)
# Generate the detailed summary
response = generate_text(outline_prompt)
print(response)
# Split the summary into individual events
event_names = response.split('--evnt--')

# Remove empty events and trim the spaces at the beginning and end of each event
event_names = [i.strip() for i in event_names if i.strip()]

print(event_names)


def intmaker(text):
    # Extract digits
    number = ''.join(filter(str.isdigit, text))
    # Convert to integer and limit to 10
    number = min(int(number), 10) if number else 0
    return number


psg = []
for i, event in enumerate(event_names):
    text = generate_text3(f"How many passages should be used here for this event {event}\n"
                          f"There should be 25 passages total"
                          f"there are {sum(psg)} passages used, and {len(event_names) - i - 1} events left"
                          f"\nreturn an int, here is an example:"
                          f"1")
    text = intmaker(text)
    psg.append(text)

print(psg)
text_array=[]

def pass_gen(summary=""):
    author = "Rick Riordan"
    style_guide = "The writing must be lively, peppered with humor and adventure, utilizing a blend of short, " \
                  "impactful phrases and longer, detailed sentences. Aim for a word count between 50 to 150 words."
    examples = ""
    summary_ex = "The speaker, a reluctant 'half-blood', issues a warning to readers. If they suspect they share this " \
                 "unique heritage, they are encouraged to embrace their parents' reassuring falsehoods and strive for " \
                 "normality. While the narrative welcomes standard readers, those who connect deeply with the tale " \
                 "are advised to step away."
    custom_prompt = f"Write an engaging introduction to a novel in the style of {author}. " \
                    f"{summary_ex} {style_guide}. " \
                    f"Do not use information not in the summary."

    print(custom_prompt)
    passage = generate_text(custom_prompt)
    return passage


for i in range(len(event_names)):
    for x in range(psg[i]):
        if text_array[0] is None:
            text=generate_text(f"There are {psg[i]} passages 50-200 words"
                  f"Given the chapter summary{response}, for the event {event_names[i]}"
                  f" for passage number {x+1} give me a detailed outline")
            sample_text=pass_gen(text)
            print(sample_text)
            text_array.append(sample_text)
        else:
            text=generate_text(f"There are {psg[i]} passages 50-200 words"
                  f"Given the chapter summary{response}, for the event {event_names[i]}"
                               f"here is the previous passage{text_array[-1]}"
                  f" for passage number {x+1} give me a detailed outline")
            sample_text=pass_gen(text)
            print(sample_text)
            text_array.append(sample_text)

#
#
# def clean_string(code):
#     """Remove unnecessary parts from the generated code"""
#     # Remove triple backticks if present
#     code = code.replace('```python', '')
#     code = code.replace('```', '')
#     return code.replace('"', '').replace("'", "")
#
# def brain(objective):
#     tasks = []
#     # Use GPT-4 to generate tasks based on the objective
#     prompt = (f"Generate Python function/class-based tasks with names for the objective: {objective}."
#               f"The functions can not call each other, but can be use each other's returns as params"
#               f"Each task should be a clearly defined programmable function or class. "
#               f"Keep the tasks to only the most essential. "
#               f"Each task should be separated by a line break. "
#               f"For each task, please define the expected inputs and return values.\n "
#               f"Example: '1. Create a function 'connect_to_database()' to connect to the database and handle errors. "
#               f"This function takes a 'connection_string' as input and returns a 'connection' object.'")
#     print(prompt)
#     response = generate_text(prompt)
#     print(response)
#     task_names = response.split('\n')
#     print(task_names)
#     main_code = []
#     usage_code = []
#     for task_name in task_names:
#         # Ignore empty task names
#         if task_name.strip() == "":
#             continue
#
#         # Use GPT-4 to generate a sanitized directory name
#         sanitized_task_name_prompt = f"Generate a concise and descriptive name for a directory based on the task: {task_name}" \
#                                      f"(The name should be alphanumeric and can contain spaces, which will be replaced with underscores.)" \
#                                      f"(The name should avoid special characters.)" \
#                                      f"(The name should accurately represent the task.)"
#         sanitized_task_name_response = generate_text(sanitized_task_name_prompt)
#
#
#
#
#
#         task_code_prompt = (f"Generate Python code for the task: '{task_name}'. "
#                             "Please provide Python code in the form of function or class definitions. "
#                             "Do not include any invocations or comments in your response."
#                             "Do not Call the function at the end")
#
#         task_code_response = generate_text(task_code_prompt)
#         print(task_code_response)
#
#
# brain("Program a tkinter app that generates math problems")
