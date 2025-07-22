FROM python:3.9

WORKDIR /code

# copy the requirements file first to leverage Docker cache
COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the application code
COPY ./app /code/app

# run the FastAPI application
CMD ["fastapi", "run", "app/main.py", "--port", "80"]