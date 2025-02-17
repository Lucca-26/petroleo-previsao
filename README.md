# Projeto de Previsão de Produção de Petróleo

Este projeto visa prever a produção de petróleo utilizando modelos de machine learning.

## Estrutura do Projeto

- `pages/`: Contém os scripts para as páginas da aplicação Streamlit.
- `scripts/`: Contém scripts auxiliares, como o script de análise de modelos.
- `notebooks/`: Contém notebooks Jupyter utilizados para exploração de dados e modelagem.
- `images/`: Armazena imagens utilizadas na aplicação.
- `.streamlit/`: Configurações do Streamlit.
- `main.py`: O ponto de entrada da aplicação.
- `requirements.txt`: Lista as dependências do projeto.
- `README.md`: Este arquivo.

## Como Executar

1.  Clone o repositório.
2.  Instale as dependências:  
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute a aplicação:  
    ```bash
    streamlit run main.py
    ```

## Observações

- Os notebooks armazenados em `notebooks/` não são carregados no Streamlit, mas podem ser utilizados para análise exploratória e modelagem de dados.
- Certifique-se de que possui o Jupyter Notebook instalado caso deseje abrir e executar os arquivos `.ipynb`.
    ```bash
    pip install notebook
    ```
