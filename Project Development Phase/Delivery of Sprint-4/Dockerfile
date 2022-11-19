  FROM python:3.8.8
  LABEL maintainer="Manoj Kumaar , 1905047@smartinternz.com"
  RUN apt-get update
  RUN mkdir /app
  WORKDIR /app
  COPY . /app
  RUN pip install -r requirements.txt
  EXPOSE 8080
  ENTRYPOINT [ "python" ]
  CMD [ "app.py" ]