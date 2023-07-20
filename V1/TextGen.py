import openai

openai.api_key = "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"


def textgen(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    message = completion["choices"][0]["message"]["content"]
    return message


def textgen3(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    message = completion["choices"][0]["message"]["content"]
    return message
