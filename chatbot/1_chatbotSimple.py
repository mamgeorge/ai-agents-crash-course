import chainlit as cl
import dotenv

dotenv.load_dotenv()

@cl.on_message
async def on_message(mesage: cl.Message):
    await cl.Message(content=f"Received: {mesage.content}").send()
