# Gerador de Código de Barras
Um mini projeto para geração de código de barras a partir de um texto.

![Imagem do código de barras gerado para o texto "image_path"](image_path.png)


## Principais ferramentas utilizadas:
- python
- flask
- virtualenv
- python-barcode
- pylint
- pre-commit
- cerberus


## Procedimentos para utilização
Realize o download do projeto em sua máquina:
```
git clone https://github.com/rad-silva/barcode-generator.git
```

Crie e ative um ambiente virtual python:
```
. .venv/bin/activate
```

Instale as dependências necessárias:
```
pip3 install -r requirements.txt
```

Rode a aplicação:
```
python3 run.py
```

Você pode usar a ferramenta Postman como auxilio para enviar uma requisição `POST` no endereço `http://localhost:3000/create_tag` contendo o texto escolhido:
```
{
    "product_code": "bar-coders-e-onde-habitam"
}
```
