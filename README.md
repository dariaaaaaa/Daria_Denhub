# WebAPI Home Task
Automated API testing with Python requests and behave  


## Project Structure:  

```
.
├── behave.ini
├── features
│   ├── 1_UploadFile.feature
│   ├── 2_GetFileMetadata.feature
│   ├── 3_DeleteFile.feature
│   ├── lib
│   │   ├── img
│   │   │   └── picture.png
│   │   ├── request_factory.py
│   │   └── request.py
│   └── steps
│       └── drx_api_tests.py
├── report.html
├── report.json
└── requirements.txt

```

### Requirements. 
##### To install requirements run in your command promt:
```
pip install -r requirements.txt
```


### To run the test with json report use:
```
behave -f json.pretty -o report/report.json
```
### To run the test with html report use:
```
behave -f html -o report/report.html
```
