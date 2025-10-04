# Dockerfile para Habitat Layout Creator
FROM python:3.11-slim

# Instala dependências do sistema para cairosvg
RUN apt-get update && apt-get install -y \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia requirements e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia código da aplicação
COPY app.py .
COPY src/ ./src/
COPY data/ ./data/

# Expõe porta do Streamlit
EXPOSE 8501

# Configura variáveis de ambiente do Streamlit
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Comando para iniciar a aplicação
CMD ["streamlit", "run", "app.py"]
