from TextGen import textgen as generate_text
from TextGen import textgen3 as generate_text3


def create_passage(summary=""):
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
                     f"{summary} {style_guide}. "
                     f"Do not use information not in the summary.")
    print(custom_prompt)
    passage = generate_text(custom_prompt)
    return passage


def produce_passages_outline(event_names, extract_integer, create_passage, chap_summary):
    # Generate passage count for each event
    passage_counts = []
    for i, event in enumerate(event_names):
        # prompt_text = (f"Consider this event in the context of a story: '{event}'.\n" f"In total, the chapter
        # should be divided into 25 passages.\n" f"So far, {sum(passage_counts)} passages have been used to cover
        # previous events.\n" f"There are {len(event_names) - i - 1} more events left to describe after this one.\n"
        # f"Assuming minor events require 1-2 passages, medium events need 2-4 passages, and major events necessitate
        # 4 or more passages, " f"how many passages should be allocated to adequately describe this event? " f"Please
        # return an integer. For example, the answer could be '1'.")
        prompt_text = (
            f"In the context of a chapter from a novel, I have divided the story into {len(event_names)} key events. "
            f"I am currently on event number {i + 1}, here is a summary of the: '{event}'.\n"
            f"So far, {sum(passage_counts)} out of a total of 25 passages have been allocated to the preceding events.\n"
            f"Taking into account that minor events typically require 1-2 passages, medium events require 2-4 "
            f"passages, and major events require 4 or more passages,"
            f"how many passages should be allocated to adequately describe this event? "
            f"Please return an integer. For example, the answer could be '1'.")

        passage_count = generate_text3(prompt_text)
        print(passage_count)
        passage_count = extract_integer(passage_count)
        passage_counts.append(passage_count)
        print(passage_count)
    print(passage_counts)
    # Generate passages for each event

    event_names = [
        'The chapter opens up with Percy Jackson on a school field trip to the Metropolitan Museum of Art. Percy and his classmates gather around the Greek and Roman exhibits, pretending to be interested, while secretly discussing their weekend plans. This is a normal routine for Percy as he navigates through his school life, unaware of the adventures lying ahead.',
        'During the field trip, Percy encounters his pre-algebra teacher, Mrs. Dodds, who is notoriously strict and demanding. He perceives her as menacing, a feeling that he usually associates with her. Their interaction underscores the dynamics of their relationship and provides context for the shocking events to come.',
        'Suddenly, Percy finds himself in a terrifying situation when Mrs. Dodds transforms into a creature from Greek mythology, a Fury. This shocking reveal occurs in the isolated space of the museum, with Percy finding himself the target of this monstrous transformation. The fear and disbelief Percy feels emphasize the otherworldliness of the situation and throws him into the unknown world of Greek mythology.',
        'His Latin teacher, Mr. Brunner, saves Percy by throwing him a pen that magically transforms into a sword. This reveal forms the first understanding the reader has of Mr. Brunner\'s role in Percy\'s life – not just as a mentor, but as a protector. Percy, although fearful, bravely uses the sword to defeat the Fury, marking his entry into a world of fantasy and danger he previously knew nothing about.',
        'After the attack, Percy finds himself in a disturbing reality where no one remembers Mrs. Dodds. Instead, they believe a woman named Mrs. Kerr, whom Percy has never met, is their pre-algebra teacher. This memory alteration terrifies Percy and his confusion, fear, and disbelief grow, throwing light on the powerful forces the protagonist is up against.',
        'Finally, Percy overhears a worrying conversation between Mr. Brunner and his friend Grover. The secretive conversation stirs Percy\'s suspicion and fear, leaving him more unsettled than before. This conversation adds to the mystery and uncertainty surrounding Percy\'s sudden encounter with the mythical world, providing a suspenseful end to the chapter and setting the stage for the adventures to come.'
    ]

    chap_summary = "\n".join(event_names)
    print(chap_summary)
    print(event_names)

    passages_outlines = []
    for i in range(len(event_names)):
        for j in range(passage_counts[i]):
            if len(passages_outlines) == 0:  # If this is the first passage
                narrative_prompt = (f"Based on the chapter summary {chap_summary} and event {event_names[i]}, "
                                    f"write a narrative introducing the situation.")
                passages_outline = generate_text(narrative_prompt)
                passages_outlines.append(passages_outline)
            else:
                narrative_prompt = (f"Given the chapter summary {chap_summary}, event {event_names[i]} "
                                    f"and the previous narrative: '{passages_outlines[-1]}', "
                                    f"continue the story with a new passage.")
                passages_outline = generate_text(narrative_prompt)
                passages_outlines.append(passages_outline)
            print(passages_outline)

    return passages_outlines


