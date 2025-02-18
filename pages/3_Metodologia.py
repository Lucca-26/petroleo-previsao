import streamlit as st

st.set_page_config(page_title="Metodologia", page_icon="🛠️")

st.title("🛠️ Metodologia do Projeto")

st.write("""
Esta página detalha a metodologia completa utilizada no desenvolvimento deste projeto de análise e previsão das oscilações do preço do petróleo Brent.
Abordaremos desde a coleta de dados até a implantação do modelo, passando pelas ferramentas, técnicas e testes realizados.
""")

st.header("1. Ferramentas Utilizadas")

st.write("""
Para o desenvolvimento deste projeto, utilizamos as seguintes ferramentas:

- **Linguagem de Programação:**
    - **Python:** Linguagem de programação de alto nível, versátil e amplamente utilizada em ciência de dados e Machine Learning devido à sua vasta gama de bibliotecas e frameworks.

- **Bibliotecas Python:**
    - **yfinance:** Biblioteca para coletar dados financeiros do Yahoo Finance, utilizada para obter os dados históricos do petróleo Brent.
    - **pandas:** Biblioteca para manipulação e análise de dados, utilizada para criar e manipular DataFrames.
    - **numpy:** Biblioteca para computação numérica, utilizada para realizar operações matemáticas e estatísticas.
    - **scikit-learn:** Biblioteca de Machine Learning, utilizada para treinar e avaliar os modelos de previsão.
    - **tensorflow/keras:** Frameworks de Deep Learning, utilizados para construir e treinar o modelo LSTM.
    - **streamlit:** Biblioteca para criar aplicativos web interativos, utilizada para construir a interface do usuário do projeto.
    - **plotly:** Biblioteca para criação de gráficos interativos, utilizada para visualizar os dados e os resultados dos modelos.
    - **seaborn:** Biblioteca para visualização de dados, utilizada para criar gráficos estatísticos.
    - **xgboost:** Biblioteca para Gradient Boosting, utilizada para treinar o modelo XGBoost.

- **Ambiente de Desenvolvimento:**
    - **Visual Studio Code (VS Code):** Editor de código leve e poderoso, utilizado para escrever e depurar o código Python.

- **Controle de Versão:**
    - **Git:** Sistema de controle de versão distribuído, utilizado para gerenciar as alterações no código e colaborar com outros desenvolvedores.
    - **GitHub:** Plataforma de hospedagem de código Git, utilizada para armazenar e compartilhar o código do projeto.

- **Implantação (Deploy):**
    - **Streamlit Cloud:** Plataforma para implantar aplicativos Streamlit na nuvem, utilizada para disponibilizar o projeto online.
""")

st.header("2. Coleta e Pré-Processamento de Dados")

st.write("""
A coleta e o pré-processamento dos dados foram etapas cruciais para garantir a qualidade e a adequação dos dados para a modelagem.

- **Coleta de Dados:**
    - Utilizamos a biblioteca `yfinance` para coletar dados históricos do preço do petróleo Brent (ticker: BZ=F) diretamente do Yahoo Finance.
    - Os dados coletados incluem: data, preço de abertura, preço máximo, preço mínimo, preço de fechamento e volume.

- **Pré-Processamento de Dados:**
    1. **Tratamento de Valores Ausentes:** Removemos as linhas com valores ausentes para evitar erros nos modelos.
    2. **Detecção e Remoção de Outliers:** Utilizamos o método IQR (Intervalo Interquartil) para identificar e remover outliers nas variáveis numéricas.
    3. **Criação de Variáveis Derivadas (Feature Engineering):** Criamos novas variáveis a partir dos dados existentes para melhorar a capacidade preditiva dos modelos, incluindo:
        - **Médias Móveis (Moving Averages):** Calculamos as médias móveis de 5 e 10 dias para suavizar as flutuações nos preços.
        - **Desvio Padrão (Standard Deviation):** Calculamos o desvio padrão de 5 dias para medir a volatilidade dos preços.
        - **Variação Diária (Daily Change):** Calculamos a variação percentual diária dos preços.

- **Variáveis Utilizadas:**
    - **Variáveis Independentes (Features):**
        - `Open`: Preço de abertura do petróleo no dia.
        - `High`: Preço máximo do petróleo no dia.
        - `Low`: Preço mínimo do petróleo no dia.
        - `Close`: Preço de fechamento do petróleo no dia.
        - `Moving_Avg_5`: Média móvel de 5 dias do preço de fechamento.
        - `Moving_Avg_10`: Média móvel de 10 dias do preço de fechamento.
        - `Std_Dev_5`: Desvio padrão de 5 dias do preço de fechamento.
        - `Daily_Change`: Variação percentual diária do preço de fechamento.
    - **Variável Dependente (Target):**
        - `Target`: Preço de fechamento do petróleo no dia seguinte (variável a ser prevista).
""")

st.header("3. Modelagem e Avaliação")

st.write("""
A etapa de modelagem envolveu a seleção, treinamento e avaliação de diferentes modelos de Machine Learning para prever o preço do petróleo Brent.

- **Modelos Utilizados:**
    1. **Regressão Linear:** Modelo linear simples que estabelece uma relação linear entre as variáveis independentes e a variável dependente.
    2. **Random Forest:** Modelo de ensemble que combina várias árvores de decisão para melhorar a precisão e reduzir o overfitting.
    3. **XGBoost (Extreme Gradient Boosting):** Modelo de Gradient Boosting que utiliza técnicas de regularização para evitar o overfitting e melhorar o desempenho.
    4. **LSTM (Long Short-Term Memory):** Modelo de rede neural recorrente (RNN) que é adequado para modelar dados sequenciais, como séries temporais.

- **Testes Realizados:**
    1. **Teste com Variável de Volume:** Avaliamos a influência da variável de volume nos modelos, dado que apresentou baixa correlação com o Target.
    2. **Análise de Períodos de Crise:** Avaliamos o desempenho dos modelos durante períodos de crise econômica e alta volatilidade (ex: crise de 2008).
    3. **Teste Geral:** Avaliamos o desempenho geral dos modelos no conjunto completo de dados.

- **Divisão dos Dados:**
    - Dividimos os dados em conjuntos de treinamento (80%) e teste (20%) para treinar os modelos e avaliar seu desempenho em dados não vistos.
    - Utilizamos a função `train_test_split` do scikit-learn para realizar a divisão dos dados.

- **Métricas de Avaliação:**
    - Utilizamos as seguintes métricas para avaliar o desempenho dos modelos:
        - **MAE (Mean Absolute Error):** Erro absoluto médio, que mede a magnitude média dos erros.
        - **RMSE (Root Mean Squared Error):** Raiz do erro quadrático médio, que mede a magnitude média dos erros, dando mais peso aos erros maiores.
        - **R² (R-squared):** Coeficiente de determinação, que mede a proporção da variância da variável dependente que é explicada pelas variáveis independentes.

- **Resultados dos Testes:**
    - Os resultados dos testes foram os seguintes:
        ```
        🔹 Modelo: XGBoost
        MAE: 1.69
        RMSE: 2.36
        R²: 95.76%

        🔹 Modelo: Random Forest
        MAE: 1.62
        RMSE: 2.27
        R²: 96.07%

        🔹 Modelo: Regressão Linear
        MAE: 1.45
        RMSE: 2.07
        R²: 96.75%

        ➡️ Treinando LSTM...
        Epoch 1/20
        ...
        Epoch 20/20

        🔹 Modelo: LSTM
        MAE: 14.70
        RMSE: 15.09
        R²: -72.97%
        ```

- **Seleção do Modelo:**
    - Após avaliar os resultados dos testes, **escolhemos o modelo de Regressão Linear como o mais adequado para este projeto.**
    - **Motivo da Escolha:**
        - O modelo de Regressão Linear apresentou o melhor desempenho em termos de R² (96.75%), indicando que ele explica a maior parte da variância da variável dependente.
        - Além disso, o modelo de Regressão Linear apresentou os menores valores de MAE (1.45) e RMSE (2.07), indicando que ele tem a menor magnitude média dos erros.
        - Apesar de modelos mais complexos como Random Forest e XGBoost terem desempenhos competitivos, o modelo de Regressão Linear oferece uma combinação de precisão e simplicidade que o torna ideal para este projeto.
        - O modelo LSTM apresentou um desempenho muito inferior aos demais, com um R² negativo, indicando que ele não é adequado para este problema.
""")

st.header("4. Implantação (Deploy) do Projeto")

st.write("""
A implantação do projeto envolveu a criação de um aplicativo Streamlit interativo e a sua disponibilização online através do Streamlit Cloud.

- **Estrutura do Projeto:**
    - O projeto foi estruturado em um repositório Git com os seguintes arquivos e pastas:
        - `main.py`: Arquivo principal do aplicativo Streamlit.
        - `pages/`: Pasta contendo os arquivos das páginas do aplicativo.
        - `scripts/`: Pasta contendo os scripts Python com as funções de análise e modelagem.
        - `requirements.txt`: Arquivo com a lista das bibliotecas Python necessárias para executar o projeto.
        - `README.md`: Arquivo com a descrição do projeto.

- **Passos para Executar o Projeto Localmente:**
    1. **Clonar o Repositório:**
       - Clone o repositório Git para o seu computador utilizando o seguinte comando:
         ```bash
         git clone https://github.com/SEU_USUARIO/petroleo-previsao.git
         ```
    2. **Criar um Ambiente Virtual:**
       - Crie um ambiente virtual Python para isolar as dependências do projeto:
         ```bash
         python -m venv venv
         ```
    3. **Ativar o Ambiente Virtual:**
       - Ative o ambiente virtual:
         - No Windows:
           ```bash
           venv\\Scripts\\activate
           ```
         - No Linux/macOS:
           ```bash
           source venv/bin/activate
           ```
    4. **Instalar as Dependências:**
       - Instale as bibliotecas Python necessárias a partir do arquivo `requirements.txt`:
         ```bash
         pip install -r requirements.txt
         ```
    5. **Executar o Aplicativo Streamlit:**
       - Execute o aplicativo Streamlit utilizando o seguinte comando:
         ```bash
         streamlit run main.py
         ```
    6. **Acessar o Aplicativo:**
       - O aplicativo será aberto automaticamente no seu navegador. Caso contrário, acesse o endereço exibido no terminal (geralmente `http://localhost:8501`).

- **Deploy no Streamlit Cloud:**
    1. **Criar uma Conta no Streamlit Cloud:**
       - Acesse [Streamlit Cloud](https://streamlit.io/cloud) e crie uma conta.
    2. **Conectar o Repositório GitHub:**
       - Conecte o seu repositório GitHub ao Streamlit Cloud.
    3. **Configurar o Aplicativo:**
       - Selecione o arquivo `main.py` como o arquivo principal do aplicativo.
       - Especifique as dependências do projeto no arquivo `requirements.txt`.
    4. **Implantar o Aplicativo:**
       - Clique no botão "Deploy" para implantar o aplicativo no Streamlit Cloud.
       - O Streamlit Cloud irá construir o aplicativo e disponibilizá-lo online.

- **Acesso ao Aplicativo:**
    - Após a implantação, o aplicativo estará acessível através de um URL fornecido pelo Streamlit Cloud.
""")

st.header("5. Conclusão")

st.write("""
Este projeto demonstrou a viabilidade de utilizar técnicas de Machine Learning para analisar e prever as oscilações do preço do petróleo Brent.
Através da combinação de coleta de dados, pré-processamento, modelagem e visualização interativa, foi possível criar uma ferramenta útil e acessível
para entender as dinâmicas do mercado de petróleo.

A escolha do modelo de Regressão Linear, com base nos resultados dos testes, permitiu obter um bom desempenho com um modelo simples e interpretabilidade.
As ferramentas e metodologias utilizadas neste projeto podem ser aplicadas a outros problemas de previsão e análise de dados,
contribuindo para a tomada de decisões mais informadas e eficientes.
""")

# Botões de navegação
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Voltar"):
        st.switch_page("pages/2_Objetivo.py")

with col2:
    if st.button("➡ Ir Para Análise"):
        st.switch_page("pages/4_Analise.py")