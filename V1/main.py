from event_generator import generate_event_summary
from passage_generator import create_passage, produce_passages_outline
from NLP import extract_integer




# The summary of the chapter
brief_summary = "In this chapter, the protagonist Percy Jackson goes on a school field trip " \
                "to the Metropolitan Museum of Art, where he encounters his pre-algebra teacher " \
                "Mrs. Dodds. Unexpectedly, Mrs. Dodds transforms into a Fury from Greek mythology " \
                "and attacks him. Percy is saved by his Latin teacher, Mr. Brunner, who throws " \
                "him a magical pen that transforms into a sword, which he uses to defeat the Fury. " \
                "However, after the attack, Percy finds that everyone's memories have been altered, " \
                "and no one remembers Mrs. Dodds. Instead, they believe a woman named Mrs. Kerr, " \
                "whom Percy has never seen before, has always been their pre-algebra teacher. " \
                "The chapter concludes with Percy overhearing a worrying conversation between " \
                "Mr. Brunner and his friend Grover, adding to his confusion and fear."


# Call the function
# event_names, chap_summary = generate_event_summary(brief_summary)

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

# Generate passages
passages = produce_passages_outline(event_names, extract_integer, create_passage, chap_summary)
