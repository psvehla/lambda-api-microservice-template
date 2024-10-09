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
