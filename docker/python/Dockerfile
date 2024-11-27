FROM python:3.8.5

# Configurar la variable de entorno para evitar problemas de buffer
ENV PYTHONUNBUFFERED 1

# Crear y configurar el directorio de trabajo
RUN mkdir /workspace
WORKDIR /workspace

# Copiar el archivo de requisitos
ADD requirements.txt /workspace/

# Actualizar pip y desactivar la verificación SSL en la instalación
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --timeout=120 --index-url=https://pypi.org/simple -r requirements.txt

# Copiar el resto de los archivos al contenedor
ADD . /workspace/
