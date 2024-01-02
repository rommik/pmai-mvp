from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import openai
import gradio as gr
import os


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

with gr.Blocks() as demo:
    gr.Markdown("# PMAI MVP")
    with gr.Tab("PM"):
       gr.Markdown("Chat here")

    with gr.Tab("Project"):
        gr.Markdown("Project Info here")
    with gr.Tab("Memory"):
        gr.Markdown("Assistant Memory")

if __name__ == "__main__":
    demo.launch()