# Selenium Home Task (variant 2)
Automation with Selenium webdriver, python, behave  

## Project Structure:  

```
.
├── behave.ini
├── features
│   ├── add_job_title.feature
│   ├── delete_job.feature
│   ├── edit_job.feature
│   ├── environment.py
│   ├── lib
│   │   └── pages
│   │       ├── admin_page.py
│   │       ├── base_page.py
│   │       ├── dashboard_page.py
│   │       ├── jobtitle_list_page.py
│   │       ├── login_page.py
│   │       └── save_jobtitle_page.py
│   └── steps
│       └── job.py
├── report.html
├── report.json
└── requirements.txt
  
```

### Requirements. 
##### To install requirements run in your command promt:
```
pip install -r requirements.txt
```
##### Also you need to download ChromeDriver and add its path to the environment variables.  


### To run the test with json report use:
```
behave -f json.pretty -o report.json
```
### To run the test with html report use:
```
behave -f html -o report.html
```
