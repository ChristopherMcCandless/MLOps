FROM python:3.8-slim
WORKDIR /streamlit_app
COPY . /streamlit_app
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "streamlit_startup.py"]