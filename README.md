# A example for preparing sif file for singularity

## 1. Dockerfile

A example docker file:

```dockerfile
FROM alpine:3.17.3

# Install python3 and other dependencies
RUN apk add --no-cache python3 py3-pip

RUN pip3 install jinja2-cli[yaml,toml,xml,hjson,json5]==0.8.2 pyyaml
ADD ./jinja_process.py /usr/local/bin/
ENTRYPOINT ["python", "/usr/local/bin/jinja_process.py"]
```

## 2. Docker build

```bash
git clone https://github.com/huboqiang/jinja2_config
docker build --platform linux/amd64 -t jinja_config:v0-amd64 jinja2

## optional, push dockerhub, https://hub.docker.com/repository/docker/hubq/jinja2_jhuang_config
docker tag jinja_config:v0-amd64 hubq/jinja2_jhuang_config:v0-amd64
docker push hubq/jinja2_jhuang_config:v0-amd64
```

## 3. Convert docker image into singularity

```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/projects/WDL/singularity:/output \
    --privileged -t --rm \
    quay.io/singularity/docker2singularity \
    jinja_config:v0-amd64
```

## 4. Run in cluster

```bash
./jinja_config_v0-amd64.sif config.yaml
```

Result:

```
#./jinja_config_v0-amd64.sif ./config.yaml
colors:
  NEJM_set: ["#0172B6", "#E18727", "#BD3C29"]
project:
  my_proj:
    my_dataset:
      geneder:
        male:   "#0172B6" # "#0172B6"
        female: "#BD3C29" # "#BD3C29"
```

## 5. Using jinja2 in R via singularity sif image

```R
result <- system("./jinja_config_v0-amd64.sif config.yaml", intern = TRUE)
yaml::yaml.load(result)
```
