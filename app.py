from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("サンプルアプリ: 専門家に聞いてみよう！")
st.write("#### このアプリは、経営の専門家と心理学の専門家の2人の専門家に質問できるサンプルアプリです。")
st.write("##### 使い方")
st.write("①どちらの専門家に聞くか選択してください。  \n②入力フォームにテキストを入力して「実行」ボタンを押すと、選択した専門家からの回答が表示されます。")

selected_item = st.radio(
    "専門家を選択してください。",
    ["経営の専門家", "心理学の専門家"]
)

st.divider()

input_message = st.text_input(label="専門家に聞きたい内容を入力してください。")

if st.button("実行"):
    st.divider()

    from langchain_openai import ChatOpenAI
    from langchain_core.messages import SystemMessage, HumanMessage
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

    if selected_item == "経営の専門家":
        system_message = SystemMessage(content="あなたは経営の専門家です。")
        human_message = HumanMessage(content=input_message)
        response = llm([system_message, human_message]) 
        st.write("### 経営の専門家からの回答")
        st.write(response.content)

    elif selected_item == "心理学の専門家":
        system_message = SystemMessage(content="あなたは心理学の専門家です。")      
        human_message = HumanMessage(content=input_message)
        response = llm([system_message, human_message])
        st.write("### 心理学の専門家からの回答")
        st.write(response.content)
        
    else:
        st.error("専門家に聞きたい内容を入力してから「実行」ボタンを押してください。")
