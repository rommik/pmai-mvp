from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import openai
import gradio as gr
import os
import random
import time
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo-0613')

# def predict(message, history):
#     history_langchain_format = []
#     for human, ai in history:
#         history_langchain_format.append(HumanMessage(content=human))
#         history_langchain_format.append(AIMessage(content=ai))
#     history_langchain_format.append(HumanMessage(content=message))
#     gpt_response = llm(history_langchain_format)
#     return gpt_response.content

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

def get_votes():
    return '/n'.join(votes)

with gr.Blocks() as demo:
   
    gr.Markdown("# PMAI MVP")
    with gr.Tab("PM"):

        chatbot = gr.Chatbot()
       
        msg = gr.Textbox()
        clear = gr.Button("Clear")

        def user(user_message, history):
            return "", history + [[user_message, None]]

        def bot(history):
            bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
            history[-1][1] = ""
            for character in bot_message:
                history[-1][1] += character
                time.sleep(0.05)
                yield history

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        
        
        clear.click(lambda: None, None, chatbot, queue=False)

    with gr.Tab("Project"):
        gr.Markdown("Project Info here")
    with gr.Tab("Memory"):
       gr.Markdown("Memory here")
       votes_history = gr.Textbox(label="Votes")
       chatbot.like(add_vote, None, outputs=votes_history)
        
        
        

if __name__ == "__main__":
    demo.queue()
    demo.launch()