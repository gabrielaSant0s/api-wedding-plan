# Use an official Python runtime as the base image
# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt /code/

# Install the project dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project code to the working directory
COPY . /code/

# Expose the port where the Django development server will run
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

