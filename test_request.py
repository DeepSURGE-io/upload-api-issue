import requests

if __name__ == "__main__":
    # make a test request, upload a file to the graphql endpoint
    endpoint = "http://localhost:8001/graphql2"
    res = requests.post(endpoint, files={
        "operations": (None, '{ "query": "mutation($file: Upload!){ uploadFile(file: $file) }", "variables": { "file": null } }'),
        "map": (None, '{ "file": ["variables.file"] }'),
        "file": ('text.txt', open("test.txt", "rb"))
        })
    print(res.status_code)

    res = requests.post(endpoint, files={
        "operations": (None, '{ "query": "mutation($files: [Upload!]!){ uploadFiles(files: $files) }", "variables": { "files": [null] } }'),
        "map": (None, '{ "file1": ["variables.files.0"]}'),
        "file1": ('text.png', open("1200px-Flag_of_the_United_States.png", "rb"))
        })
    print(res.status_code)