FROM python:3.9-slim

# Create app directory
RUN mkdir /app
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source
COPY . .

# Expose the port
EXPOSE 5000

# Run the app
CMD ["flask", "run", "--host=0.0.0.0"]