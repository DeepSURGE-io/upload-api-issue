# upload-api-issue
 standalone repo to reproduce "Unknown type 'Upload'"

## Creating the environment

Dependencies for this repo is contained in an Anaconda environment, set it up with the command below:

```
conda env create --name fastapi-strawberry-env -f env.yml
```

Update the env

```
conda env update --name fastapi-strawberry-env --file env.yml  --prune
```

Run the server with the following commands

```
uvicorn src.main:app --reload
```
