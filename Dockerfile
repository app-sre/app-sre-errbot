FROM registry.access.redhat.com/ubi8/python-36

RUN pip3 install -U pip setuptools && \
    pip3 install virtualenv 

COPY requirements.txt /opt/app-root/src
RUN virtualenv /opt/app-root/src/venv
RUN . /opt/app-root/src/venv/bin/activate && \
    pip install --no-cache-dir -r /opt/app-root/src/requirements.txt

RUN mkdir -p /opt/app-root/errbot/{data,plugins}

COPY config.py /opt/app-root/errbot
COPY run.sh /opt/app-root/errbot

WORKDIR /opt/app-root/errbot

ENTRYPOINT ["/opt/app-root/errbot/run.sh"]
CMD ["errbot"]
