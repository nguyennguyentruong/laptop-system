FROM python

COPY . /app

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "flask", "--app", "main", "run"]

EXPOSE 5000