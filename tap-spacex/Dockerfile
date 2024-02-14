FROM meltano/meltano:latest

WORKDIR /project

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN meltano install
RUN meltano invoke airflow:create-admin --username admin \
    --password admin \
    --email admin@example.com \
    --firstname admin \
    --lastname admin \
    --role Admin
ENV MELTANO_PROJECT_READONLY 1

EXPOSE 5000

ENTRYPOINT ["meltano"]
