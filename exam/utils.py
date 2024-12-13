import os
from groq import Groq


def evalute(answers):
    client = Groq(
        api_key="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"
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system",
             "content": "You are a teacher. Evaluate the student's performance on a scale of 100 and return only the percentage score. For example - 30%. answer on russian "},
            {
                "role": "user",
                "content": f"{answers}",
            }
        ],
        model="llama3-8b-8192",
    )

    # Извлекаем текст из ответа
    content = chat_completion.choices[0].message.content.strip()
    print(f"Raw response from API: {content}")

    # Проверяем, что ответ корректен
    if not content.endswith('%'):
        raise ValueError(f"Unexpected response format: {content}")

    return content  # Например, "50%"
