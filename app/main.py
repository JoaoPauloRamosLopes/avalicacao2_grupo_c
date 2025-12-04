import os
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# VULNERABILIDADE INTENCIONAL PARA TESTAR CODEQL
@app.get("/run-command")
def run_command(request: Request, cmd: str):
    os.system("echo " + cmd) # Command Injection
    return {"message": f"Executed command: {cmd}"}
