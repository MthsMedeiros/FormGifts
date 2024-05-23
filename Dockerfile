# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Instale dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o contêiner
COPY . .

# Defina a variável de ambiente para garantir que os logs do Flask sejam enviados para o console
ENV FLASK_ENV=production

# Exponha a porta em que a aplicação Flask será executada
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
