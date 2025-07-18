from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm  = ChatOpenAI(model="gpt-4o")

print("ChatOpenAI model initialized.")


template = "Write a {tone} email nto {company} expressing interset in the {position} position. Include a brief introduction about yourself and your skills."

prompt_template = ChatPromptTemplate.from_template(template)
print("ChatPromptTemplate initialized.")


prompt = prompt_template.invoke({
    "tone": "professional",
    "company": "Google",
    "position": "Software Engineer"
})

print("Prompt template invoked.")

res = llm.invoke(prompt)
print(res.content)