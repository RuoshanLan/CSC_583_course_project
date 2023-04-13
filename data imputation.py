import openai
import pandas as pd

openai.api_key = ""

# def few_shot():
#
#

def zero_shot():
    query = "guess what is the city?"
    return query

def read_dataset():
    df = pd.read_csv('dataset/Restaurant/zomato.csv')
    info = df.iloc[0,:-1]
    return info


def func():
    # while True:
        content = str(read_dataset()) + zero_shot()
        print(content)
        messages = [
                {"role": "system", "content": "you are a data scientist and you are doing imputation work"},
                {"role": "user", "content": content}
            ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= messages
        )
        chat_response = completion.choices[0].message.content
        print(f'ChatGPT: {chat_response}')
        messages.append({"role": "assistant", "content": chat_response})

if __name__ == '__main__':
    func()
