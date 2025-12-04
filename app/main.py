import subprocess
import shlex
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Rota segura para executar comandos
@app.get("/run-command")
def run_command(cmd: str):
    """
    Executa um comando de forma segura.
    
    Args:
        cmd: Comando a ser executado (apenas comandos na lista permitida)
        
    Returns:
        dict: Resultado da execução do comando
        
    Raises:
        HTTPException: Se o comando não for permitido ou ocorrer um erro
    """
    # Lista de comandos permitidos (whitelist)
    ALLOWED_COMMANDS = ["echo", "ls", "pwd"]
    
    try:
        # Divide o comando em argumentos de forma segura
        args = shlex.split(cmd)
        
        # Verifica se o comando está na lista de permitidos
        if not args or args[0] not in ALLOWED_COMMANDS:
            raise HTTPException(
                status_code=400, 
                detail=f"Comando não permitido. Comandos permitidos: {', '.join(ALLOWED_COMMANDS)}"
            )
            
        # Executa o comando de forma segura
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=True,
            timeout=5,  # Timeout de 5 segundos
            shell=False  # Importante para segurança
        )
        
        return {
            "command": cmd,
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Erro ao executar o comando",
                "returncode": e.returncode,
                "stdout": e.stdout,
                "stderr": e.stderr
            }
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(
            status_code=408,
            detail="Tempo limite excedido ao executar o comando"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro inesperado: {str(e)}"
        )
