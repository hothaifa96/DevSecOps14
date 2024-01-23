FROM  python:3.11.7-alpine3.19
WORKDIR app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY main.py .
EXPOSE 6000
ENTRYPOINT [ "python3" , "main.py" ] 