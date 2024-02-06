FROM python:3.10-alpine

ADD . /app
WORKDIR /app

RUN apk --update --upgrade add --no-cache  git gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN python -m pip install --upgrade pip

# Install any dependencies
RUN pip install -r req.txt

# Specify the Flask environment port
ENV PORT 5000

# By default, listen on port 5000
EXPOSE 5000

COPY . .

CMD ["python", "app.py"]