FROM python:3.6-slim

RUN pip install scikit-learn==0.24.2
RUN pip install flask
RUN pip install pandas
RUN pip install joblib

COPY models/model.pkl /app/model.pkl
COPY app.py /app/app.py
COPY templates /app/templates


WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]