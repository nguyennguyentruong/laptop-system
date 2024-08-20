FROM python:3.10.14

RUN apt-get update && \
    apt-get install -y default-jre && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["jupyter", "notebook", "--ip", "0.0.0.0" , "--allow-root"]