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


def extract_integer(text):
    """Extracts and returns an integer from a given text. Limits the returned integer to 10."""
    number = ''.join(filter(str.isdigit, text))
    number = min(int(number), 10) if number else 0
    return number


def generate_passage(summary=""):
    """Generates and returns a passage based on a given summary."""
    author = "Rick Riordan"
    style_guide = ("The writing must be lively, peppered with humor and adventure, "
                   "utilizing a blend of short, impactful phrases and longer, detailed sentences. "
                   "Aim for a word count between 50 to 150 words.")
    summary_example = ("The speaker, a reluctant 'half-blood', issues a warning to readers. "
                       "If they suspect they share this unique heritage, they are encouraged to "
                       "embrace their parents' reassuring falsehoods and strive for normality. "
                       "While the narrative welcomes standard readers, those who connect deeply "
                       "with the tale are advised to step away.")
    custom_prompt = (f"Write an engaging introduction to a novel in the style of {author}. "
                     f"{summary_example} {style_guide}. "
                     f"Do not use information not in the summary.")
    print(custom_prompt)
    passage = generate_text(custom_prompt)
    return passage


# Generate passage count for each event
passage_counts = []
for i, event in enumerate(event_names):
    prompt_text = (f"How many passages should be used here for this event {event}\n"
                   f"There should be 25 passages total"
                   f"there are {sum(passage_counts)} passages used, and {len(event_names) - i - 1} events left"
                   f"\nreturn an int, here is an example:"
                   f"1")
    passage_count = extract_integer(generate_text3(prompt_text))
    passage_counts.append(passage_count)

print(passage_counts)

# Generate passages for each event
passages = []
for i in range(len(event_names)):
    for j in range(passage_counts[i]):
        if len(passages) == 0:  # If this is the first passage
            outline_prompt = (f"There are {passage_counts[i]} passages 50-200 words"
                              f"Given the chapter summary {response}, for the event {event_names[i]}"
                              f" for passage number {j+1} give me a detailed outline")
            passage = generate_passage(outline_prompt)
            print(passage)
            passages.append(passage)
        else:
            outline_prompt = (f"There are {passage_counts[i]} passages 50-200 words"
                              f"Given the chapter summary {response}, for the event {event_names[i]}"
                              f"Here is the previous passage {passages[-1]}"
                              f" for passage number {j+1} give me a detailed outline")
            passage = generate_passage(outline_prompt)
            print(passage)
            passages.append(passage)