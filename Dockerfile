# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Atualize pip e instale dependências do sistema necessárias com depuração
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --upgrade pip setuptools wheel

# Verifique se as dependências do sistema foram instaladas corretamente
RUN echo "Dependências do sistema instaladas com sucesso."

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Verifique se as dependências do Python foram instaladas corretamente
RUN echo "Dependências Python instaladas com sucesso."

# Copie o restante do código da aplicação para o contêiner
COPY . .

# Defina a variável de ambiente para garantir que os logs do Flask sejam enviados para o console
ENV FLASK_ENV=production

# Exponha a porta em que a aplicação Flask será executada
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
