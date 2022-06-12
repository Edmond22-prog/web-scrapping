FROM python:3.10

ADD script.py .

RUN pip install requests beautifulsoup4

CMD ["python", "./script.py"]