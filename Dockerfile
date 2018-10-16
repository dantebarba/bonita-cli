FROM python:2-alpine
LABEL MANTEINER "dantebarba@gmail.com"

COPY . .

RUN pip install --upgrade pip

RUN pip install -e .[test]

ENTRYPOINT ["/entrypoint.sh"]