# A Template for an API Microservice That Runs as a Lambda

```bash
fastapi-codegen --input openapi.yaml --output app --generate-routers --output-model-type pydantic_v2.BaseModel
```

Correct incorrectly generated field name for `x-logo` in line 20 of `main.py`.

```bash
fastapi dev app/main.py
```
