# Meu FastAPI do Zero

Minha versão do código do curso [FastAPI do Zero](https://fastapidozero.dunossauro.com/).

As principais diferenças são:

- Utilização do [Dev Containers](https://containers.dev/) para a criação automática do ambiente de desenvolvimento integrado ao [Visual Studio Code](https://code.visualstudio.com/).

## Como Executar?

Esse projeto requer as seguintes ferramentas instaladas:

- [Podman](https://podman.io/) (opção com Docker será apresentada mais a diante)
- [Visual Studio Code](https://code.visualstudio.com/Download)
- Plugin [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Após isso, ao abrir o projeto no VS Code, será sugerido abrir o projeto dentro de um contêiner, ao aceitar, todo o ambiente necessário para desenvolver a aplicação será criado.

### Dev Containers no Docker

Também é possível usar esse projeto com [Docker](https://www.docker.com/) no lugar do Podman, porém para isso é necessário editar o arquivo `.devcontainer/devcontainer.json` removendo o atributo `runArgs` junto com sua lista de valores. Após isso, basta abrir o projeto no VS Code e concordar em reabri-lo dentro de um contêiner.
