FROM python
WORKDIR tests_api
COPY . .
RUN pip install -r requirements.txt
CMD pytest -s -v tests_api/tests.py .
