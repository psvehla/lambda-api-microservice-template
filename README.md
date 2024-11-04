# A Template for an API Microservice That Runs as a Lambda

## How This Template Was Put Together

Grab `openapi.yaml` from [here](https://github.com/psvehla/openapi-template/blob/peter/openapi.yaml).

Generate Facade layer.

```bash
fastapi-codegen --input openapi.yaml --output app --generate-routers --output-model-type pydantic_v2.BaseModel
```

Correct incorrectly generated field name for `x-logo` in line 20 of `main.py`.

Test run.

```bash
fastapi dev app/main.py
```

Lambda build.

```bash
mkdir lambda-build

docker run --platform linux/amd64 -u $(id -u):$(id -g) -v ./lambda-build:/lambda-build -v ./requirements.txt:/requirements.txt -v ~/.cache/pip:/.cache/pip python:3.12 pip install -r /requirements.txt -t /lambda-build

cp -r app lambda-build

cd lambda-build

zip -r function.zip *
```
