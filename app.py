from fastapi import FastAPI
from chat.rebecca import Rebecca_ai

router = FastAPI()



@router.get("/")
def read_root():
    return {"Mensagem": "Olá! Eu sou a Rebecca, uma IA que sabe quase nada sobre tudo."}

@router.get("/chat/{auth}/{question}")
def read_item(question: str, auth:str):
    ai = Rebecca_ai()
    is_authenticate = ai.check_auth(auth)
    
    response = ai.chat(question, is_authenticate)
    
    return response

    
    