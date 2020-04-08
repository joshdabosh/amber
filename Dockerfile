FROM python:3.6.3

COPY amber/ /amber
WORKDIR /amber

RUN pip3 install -r requirements.txt

CMD ["python3", "amber.py"]
