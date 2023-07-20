from TextGen import textgen


# TODO Passage generation

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
    passage = textgen(custom_prompt)
    return passage


print(pass_gen())


# TODO Chapter Summary

class ChapterPlanner:
    def __init__(self, events, chapter_summary):
        self.events = chapter_summary
        self.events = events

    def event_breakdown(self):
        # TODO Event Breakdown
        pass


# TODO Event Breakdown

def brain(objective):
    tasks = []
    # Use GPT-4 to generate tasks based on the objective
    prompt = (f"Generate Python function/class-based tasks with names for the objective: {objective}."
              f"The functions can not call each other, but can be use each other's returns as params"
              f"Each task should be a clearly defined programmable function or class. "
              f"Keep the tasks to only the most essential. "
              f"Each task should be separated by a line break. "
              f"For each task, please define the expected inputs and return values.\n "
              f"Example: '1. Create a function 'connect_to_database()' to connect to the database and handle errors. "
              f"This function takes a 'connection_string' as input and returns a 'connection' object.'")
