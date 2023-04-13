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
    df = pd.read_csv('dataset/Amazon-GoogleProducts/Amazon_GoogleProducts_perfectMapping.csv')
    dfA = pd.read_csv('dataset/Amazon-GoogleProducts/Amazon.csv',encoding='cp1252')
    dfB = pd.read_csv('dataset/Amazon-GoogleProducts/GoogleProducts.csv', encoding='cp1252')
    mergedA = pd.merge(df, dfA, right_on="id", left_on="idAmazon")
    merged = pd.merge(
        mergedA,
        dfB,
        right_on="id",
        left_on="idGoogleBase",
        suffixes=("_A", "_B"),
    )

    info = merged.iloc[0,:-1]
    return info

def func():
    # while True:
        content = str(read_dataset()) + zero_shot()
        print(content)
        # messages = [
        #         {"role": "system", "content": "you are a data scientist and you are doing imputation work"},
        #         {"role": "user", "content": content}
        #     ]
        # completion = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages= messages
        # )
        # chat_response = completion.choices[0].message.content
        # print(f'ChatGPT: {chat_response}')
        # messages.append({"role": "assistant", "content": chat_response})

if __name__ == '__main__':
    func()
