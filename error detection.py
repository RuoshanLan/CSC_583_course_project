import openai
import pandas as pd
#Holistic Data Cleaning: Putting Violations Into  http://www.hospitalcompare.hhs.gov/, 2012
#https://archive.ics.uci.edu/ml/datasets/Adult
openai.api_key = ""

# def few_shot():
#
#

def zero_shot():
    query = "Is there a spelling error in this data?"
    return query

def read_dataset():
    df = pd.read_csv('dataset/adult.data',names=["workclass","fnlwgt","education","education-num","maritalstatus","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","income"])
    info = df.iloc[0]
    return info

def func():
    # while True:
        content = str(read_dataset()) #+ zero_shot()
        print(content)
        messages = [
                {"role": "system", "content": "you are a data scientist and you are doing error detection work"},
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
