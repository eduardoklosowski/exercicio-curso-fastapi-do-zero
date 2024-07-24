# Meu FastAPI do Zero

Minha versão do código do curso [FastAPI do Zero](https://fastapidozero.dunossauro.com/).

As principais diferenças são:

- Utilização do [Dev Containers](https://containers.dev/) para a criação automática do ambiente de desenvolvimento integrado ao [Visual Studio Code](https://code.visualstudio.com/).
- Utilização do [GNU Make](https://www.gnu.org/software/make/) no lugar do [taskipy](https://pypi.org/project/taskipy/), o que possibilita a execução em paralelo das ferramentas.

## Como Executar?

Esse projeto requer as seguintes ferramentas instaladas:

- [Podman](https://podman.io/) (opção com Docker será apresentada mais a diante)
- [Visual Studio Code](https://code.visualstudio.com/Download)
- Plugin [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Após isso, ao abrir o projeto no VS Code, será sugerido abrir o projeto dentro de um contêiner, ao aceitar, todo o ambiente necessário para desenvolver a aplicação será criado.

### Dev Containers no Docker

Também é possível usar esse projeto com [Docker](https://www.docker.com/) no lugar do Podman, porém para isso é necessário editar o arquivo `.devcontainer/devcontainer.json` removendo o atributo `runArgs` junto com sua lista de valores. Após isso, basta abrir o projeto no VS Code e concordar em reabri-lo dentro de um contêiner.

### Executar Testes no Commit (Opcional)

É possível configurar o repositório para executar os lints e testes antes de cada commit, dessa forma o git só fará o commit caso essas ferramentas não identifiquem problemas (nenhuma regra de lint sendo quebrada e testes passando), caso contrário o git não realizará o commit, dando a possibilidade de corrigir o erro antes de tentar fazer o commit novamente (ou o parâmetro `--no-verify` seja usado no `git commit`).

Para ativar essa verificação basta executar os comandos a baixo na raiz do projeto:

```sh
cat > .git/hooks/pre-commit << EOF
#!/bin/sh
make lint test
EOF
chmod +x .git/hooks/pre-commit
```

Caso queira agilizar o processo, é possível executar as ferramentas de verificação em paralelo, porém a saída delas poderá ficar embaralhada. Para configurar a execução do número de ferramentas igual ao número de núcleos de CPU disponível, basta usar o parâmetro `-j` do `make`, como no exemplo a seguir:

```sh
cat > .git/hooks/pre-commit << EOF
#!/bin/sh
make -j lint test
EOF
chmod +x .git/hooks/pre-commit
```
