FROM alpine:3.17.3

# Install python3 and other dependencies
RUN apk add --no-cache python3 py3-pip

RUN pip3 install jinja2-cli[yaml,toml,xml,hjson,json5]==0.8.2 pyyaml
ADD ./jinja_process.py /usr/local/bin/
ENTRYPOINT ["python", "/usr/local/bin/jinja_process.py"]
