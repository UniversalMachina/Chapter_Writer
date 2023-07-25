from TextGen import textgen as generate_text
from TextGen import textgen3 as generate_text3

def generate_sequence_parts(chap_summary, event_name, num_parts):
    parts = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    sequence_parts = [f'{parts[i]} part ({i+1}/{num_parts})' for i in range(num_parts)]

    sequences = ''
    for i, sequence_part in enumerate(sequence_parts):
        remaining_sequences = num_parts - (i + 1)
        # print(sequence_parts)
        sequence_prompt = (f"As an AI writing assistant, your task is to construct the {sequence_part} of a "
                           f"sequence of events from a provided summary. Your output should be ultra-concise, "
                           f"brief, and creative. Include only necessary details, avoid embellishments"
                           f"\n\n"
                           f"Strictly adhere to the events described in the summary—no new actions or tangents. "
                           # f"Provide a unique description of the setting and character monologues, craft creative quotes or passages, "
                           f"and outline the specific events from the summary. "
                           f"Remember to keep your output as concise as possible—eliminate any unnecessary details and do not be overly wordy. "
                           f"\n\n"
                           f"Here is an example:"
                           f"\n'A reluctant 'half-blood' narrator warns those who might be similar. "
                           f"They are urged to adhere to their parents' comforting tales and pursue normalcy. Regular readers are welcomed, those resonating with the story are advised to quit.'"
                           f"\n\n")

        if i == 0:  # 'first part (1/n)'
            sequence_prompt += (
                f"For the event: '{event_name}', generate an ultra-concise and creative sequence that covers the first part of the event.")
        elif i != num_parts - 1:  # 'middle parts (2/n to n-1/n)'
            sequence_prompt += (
                f"For the event: '{event_name}', given the previous sequences: {sequences}, continue the sequence in a concise and imaginative way, adding more details about the event.")
        else:  # 'final part (n/n)'
            sequence_prompt += (
                f"For the event: '{event_name}', given the previous sequences: {sequences}, finalize the sequence to cover the "
                f"outcome of the event in a brief and inventive manner.")

        sequence = generate_text(sequence_prompt)
        sequences += sequence + '\n'
        print(sequence)

    return sequences


# An example usage of the function:


chap_summary = ("The chapter starts with John's discovery of the secret society. This unexpected revelation takes place "
                 "in an eerie, abandoned warehouse at the outskirts of town. The silent, gigantic structure, with its "
                 "creaky wooden floorboards and dim, flickering light, adds a chilling atmosphere to the unfolding mystery. "
                 "As he ducks behind a pile of old crates, John inadvertently witnesses a secret gathering of masked "
                 "individuals engaged in an ominous ceremony. His heart pounds with fear and bewilderment, realising that "
                 "he's stumbled upon something far darker and deeper than he could ever have imagined. The implications of "
                 "this discovery are enormous for the overall plot, introducing an intricate web of conspiracy that John "
                 "must now unravel. Shortly after this discovery, John comes face to face with a conflict involving his old "
                 "friend, George. Despite the long-established camaraderie, their relationship fumbles into disagreement when "
                 "George too reveals his involvement with the secret society. The conversation happens in John's once "
                 "comforting and familiar apartment, the tension palpable between the two long-time friends. George, despite "
                 "his loyalty, defends his allegiance to the secret society, causing a rift between them that neither had "
                 "anticipated, and adding even more to the emotional stakes of the unraveling mystery. The chapter concludes "
                 "with an unexpected ally appearing in the form of Claire, John's neighbor. After his falling out with George, "
                 "John feels utterly alone until he stumbles into Claire in the building's shared laundry room. As they strike "
                 "up a conversation, she subtly hints at her knowledge of the secret society and offers her assistance. Despite "
                 "her seemingly cheery demeanor, there's also something mysterious about Claire that hints at a hidden agenda. "
                 "However, John, desperate for any help, finds solace in Claire – a character who suddenly turns from peripheral "
                 "to central. Her surprising involvement suggests a shift in alliances and provides a glimmer of hope in John's "
                 "increasingly complicated situation, thereby adding an interesting twist to the narrative.")
event_name = ("The chapter starts with John's discovery of the secret society. This unexpected revelation takes place "
                   "in an eerie, abandoned warehouse at the outskirts of town. The silent, gigantic structure, with its "
                   "creaky wooden floorboards and dim, flickering light, adds a chilling atmosphere to the unfolding mystery. "
                   "As he ducks behind a pile of old crates, John inadvertently witnesses a secret gathering of masked "
                   "individuals engaged in an ominous ceremony. His heart pounds with fear and bewilderment, realizing that "
                   "he's stumbled upon something far darker and deeper than he could ever have imagined. The implications of "
                   "this discovery are enormous for the overall plot, introducing an intricate web of conspiracy that John "
                   "must now unravel.")

num_parts = 3

sequences = generate_sequence_parts(chap_summary, event_name, num_parts)
