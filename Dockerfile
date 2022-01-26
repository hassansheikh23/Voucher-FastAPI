FROM python:3.9

WORKDIR /Voucher-API
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["uvicorn", "api:app", "--reload"]