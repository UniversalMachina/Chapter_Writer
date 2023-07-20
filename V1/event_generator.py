from TextGen import textgen as generate_text

def generate_event_summary(brief_summary):
    # The modified prompt
    outline_prompt = (f"Generate an event by event based summary for a chapter based on the following brief summary:\n"
                      f"{brief_summary}. \nThe summary should break down the main events in the chapter, "
                      f"each event should be separated by the '--evnt--' divider. Provide a detailed description "
                      f"of each event, including the characters involved, the location, any important dialogues, "
                      f"the emotional impact on the characters, and the implications for the overall plot. For example: "
                      f"\n--evnt--\nJohn's discovery of the secret society happens in an abandoned warehouse "
                      f"where he accidentally stumbles upon a secret meeting. The shock and fear he feels are palpable "
                      f"as he realizes the depth of the conspiracy he has uncovered.")
    # Generate the detailed summary
    print(outline_prompt)
    response = generate_text(outline_prompt)
    print(response)
    # Split the summary into individual events
    event_names = response.split('--evnt--')

    # Remove empty events and trim the spaces at the beginning and end of each event
    event_names = [i.strip() for i in event_names if i.strip()]
    print(event_names)
    return event_names, response
