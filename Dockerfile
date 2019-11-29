FROM python:3.7

RUN sed -i '$a \deb http://dl.google.com/linux/chrome/deb/ stable main' /etc/apt/sources.list

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        zip \
        libnss3-dev \
        google-chrome-stable \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get autoremove

RUN wget https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip \
	&& unzip chromedriver_linux64.zip \
	&& rm chromedriver_linux64.zip \
	&& mv chromedriver /usr/local/bin/chromedriver

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app

