FROM python:3.12.4-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.org

COPY . .

CMD ["python", "app.py"]
