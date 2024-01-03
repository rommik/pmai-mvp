from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from dotenv import load_dotenv
import openai
import gradio as gr
import os
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=1.0, model='gpt-4')
prompt = ChatPromptTemplate.from_messages([
    # MessagesPlaceholder(variable_name="chat_history"),
    ("system","You are world class project manager. Help the user to plan their project."),
    ("user","{input}")
    ])


output_parser = StrOutputParser()
chain = prompt | llm | output_parser
def predict(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    # gpt_response = llm(history_langchain_format)
    gpt_response = chain.invoke({"input": message})
    return gpt_response

def add_file(history, file):
    history = history + [((file.name,), None)]
    return history
votes = []
def add_vote(data: gr.LikeData):
    if data.liked:
        votes.append("You upvoted this response: " + data.value)
    else:
        votes.append("You downvoted this response: " + data.value)
    return votes


with gr.Blocks() as demo:
   
    gr.Markdown("# PMAI MVP")
    with gr.Tab("PM"):

        chat = gr.ChatInterface(predict)
        btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])
        file_msg = btn.upload(add_file, [chat, btn], [chat], queue=False)
    
    with gr.Tab("Project"):
        gr.Markdown("Project Info here")
    with gr.Tab("Memory"):
       gr.Markdown("Memory here")
       votes_history = gr.Textbox(label="Votes")
       chat.chatbot.like(add_vote, None, outputs=votes_history)
        
        
        

if __name__ == "__main__":
    demo.queue()
    demo.launch()