# Validate_address

Este projeto é um validador de endereços desenvolvido em Python, focado em garantir a qualidade dos dados de entrada através de dois métodos: validação via CEP (integração com API externa) e validação via Regex (padrão de escrita).

## 🚀 Funcionalidades

* **Validação via CEP:** Consulta em tempo real na API ViaCEP para verificar a existência do logradouro.
* **Validação de Texto:** Uso de expressões regulares (Regex) para garantir que o endereço contenha logradouro e número.
* **Interface Gráfica:** Desenvolvido com Tkinter para facilitar a interação do usuário.
* **Tratamento de Erros:** Gestão de exceções para falhas de conexão ou entradas inválidas.

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![JSON](https://img.shields.io/badge/json-5E5E5E?style=for-the-badge&logo=json&logoColor=white)

* **Python 3.x**: Linguagem principal.
* **Tkinter**: Interface gráfica (GUI).
* **Requests**: Manipulação de requisições HTTP para API ViaCEP.
* **Regex**: Expressões regulares para validação e limpeza de strings.

## 📦 Como Instalar e Rodar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/matheusebrasil/Validate_address.git](https://github.com/matheusebrasil/Validate_address.git)