FROM python:2.7
LABEL MANTEINER "dantebarba@gmail.com"

COPY . .

COPY entrypoint.sh /

RUN pip install --upgrade pip==9.0.1

RUN pip install -r requirements.txt

RUN pip install requests==2.9.1

RUN pip install -e .

ENTRYPOINT []
