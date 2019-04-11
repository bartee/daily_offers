FROM python:3.6-alpine
ADD . /code
WORKDIR /code

RUN mkdir /output_data
ENV OUTPUT_DATA_DIR /output_data

RUN make install

CMD ["python", "src/collect.py"]
VOLUME /output_data
