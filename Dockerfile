FROM python
ENV API_ID={api_id}
ENV API_HASH={api_hash}
COPY  de_d-mosk_l /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python3 runner.py










