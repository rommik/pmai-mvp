from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from dotenv import load_dotenv
import openai
import gradio as gr
import os
import random
import time
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=1.0, model='gpt-4')

def predict(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    return gpt_response.content

# gr.ChatInterface(predict).launch(auth=('user', 'password'))

def greet(name):
    return "Hello " + name + "!"
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
       
    with gr.Tab("Project"):
        gr.Markdown("Project Info here")
    with gr.Tab("Memory"):
       gr.Markdown("Memory here")
       votes_history = gr.Textbox(label="Votes")
       chat.chatbot.like(add_vote, None, outputs=votes_history)
        
        
        

if __name__ == "__main__":
    demo.queue()
    demo.launch()