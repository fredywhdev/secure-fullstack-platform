FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Crear usuario root
RUN addgroup --system app && adduser --system --ingroup app app

# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo \
    WORKDIR /app

# Copiar requirements primero \
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar el codigo \
COPY app ./app

# Cambiar permisos
RUN chown -R app:app /app

# Usar usuario no root
USER app

# Puerto interno
EXPOSE 8000

# comando de arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]