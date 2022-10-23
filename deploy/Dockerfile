FROM python:3.8.11
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 9696
ENTRYPOINT [ "streamlit", "run" ]
CMD ["app.py"]