from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()

PROJECT_ID = "lang-chain-b9525"
COLLECTION_NAME = "chat_history"

print("Initializing Firestore client...")
client= firestore.Client(project=PROJECT_ID)
print("Firestore client initialized.")

chat_history = FirestoreChatMessageHistory(
    client=client,
    collection=COLLECTION_NAME,
    session_id="test_session",
)

print("FirestoreChatMessageHistory initialized.",chat_history)

model = ChatOpenAI(model="gpt-4o")
print("ChatOpenAI model initialized.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Add user message to chat history
    chat_history.add_user_message(user_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)
    print(f"AI: {ai_response.content}")
 

