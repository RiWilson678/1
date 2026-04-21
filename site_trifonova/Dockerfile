FROM python:3.11
WORKDIR /site_trifonova
COPY requirements.txt .
RUN pip install --default-timeout=1000 -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
COPY . .
CMD ["gunicorn", "site_project.wsgi:application", "--bind", "0.0.0.0:8000"]