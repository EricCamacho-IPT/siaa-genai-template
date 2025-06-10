# Para que serve este arquivo:
# Este "hook" do Cookiecutter roda DEPOIS que o projeto é gerado.
# Ele automatiza tarefas de configuração, como criar o ambiente virtual
# e instalar as dependências corretas com base nas escolhas do usuário.

import os
import subprocess
import sys

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m"
SUCCESS = "\x1b[1;32m"
ERROR = "\x1b[1;31m"

def run_command(command, cwd):
    """Executa um comando no terminal e trata erros."""
    try:
        is_win = sys.platform == "win32"
        # No Windows, pode ser necessário `shell=True` para comandos de venv
        subprocess.run(command, check=True, cwd=cwd, shell=is_win)
        return True
    except subprocess.CalledProcessError as e:
        print(f"{ERROR}Erro ao executar: {' '.join(command)}{TERMINATOR}")
        print(e)
        return False

def is_windows():
    """Verifica se o sistema operacional é Windows."""
    return sys.platform == "win32"

def main():
    if "{{ cookiecutter.run_initial_setup }}".lower() != 'y':
        print(f"{INFO}Configuração inicial pulada. Para instalar, rode 'make install'.{TERMINATOR}")
        return

    project_directory = os.getcwd()
    python_executable = sys.executable

    print(f"{INFO}>>> Configurando ambiente virtual em '.venv'...{TERMINATOR}")
    if not run_command([python_executable, "-m", "venv", ".venv"], cwd=project_directory):
        sys.exit(1)

    # Determina os caminhos para os executáveis dentro do venv
    if is_windows():
        uv_executable = os.path.join(project_directory, ".venv", "Scripts", "uv.exe")
        pip_executable = os.path.join(project_directory, ".venv", "Scripts", "pip.exe")
        activate_command = os.path.join(".venv", "Scripts", "activate")
    else:
        uv_executable = os.path.join(project_directory, ".venv", "bin", "uv")
        pip_executable = os.path.join(project_directory, ".venv", "bin", "pip")
        activate_command = f"source {os.path.join('.venv', 'bin', 'activate')}"

    print(f"{INFO}>>> Instalando 'uv' no ambiente virtual...{TERMINATOR}")
    if not run_command([pip_executable, "install", "uv"], cwd=project_directory):
        sys.exit(1)

    print(f"{INFO}>>> Instalando dependências com 'uv'...{TERMINATOR}")
    if not run_command([uv_executable, "pip", "install", "-r", "requirements-dev.txt"], cwd=project_directory):
        sys.exit(1)

    print(f"\n{SUCCESS}🎉 Projeto configurado com sucesso! 🎉{TERMINATOR}")
    print(f"{INFO}Para ativar o ambiente virtual, rode o seguinte comando:{TERMINATOR}")
    print(f"  {activate_command}\n")

if __name__ == '__main__':
    main()
