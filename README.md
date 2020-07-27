# elector
Quick, easy and lightweight open source API for voting.

## Getting Started
In order to start elector just clone [this repository](https://github.com/Open-Sorcery/elector.git). 
Install packages listed in requirements.txt (we strongly recommend using vitrual environment):
```
pip install -r requirements.txt
```
Add settings.json file to elector/elector/elector:
```
{
    "SECRET_KEY": "<your django secret key>",
    "EMAIL": "<email address for sending access tokens>",
    "EMAIL_HOST_PASSWORD": "<email password>"
}
```
Run migrations for database:
```
python manage.py makemigrations
python manage.py migrate
```
Start server (localhost:8000):
```
python manage.py runserver
```

## API
- creating ballot `/ballot/api/create/`
- ballot details `/ballot/api/<ballot_id>/`
- voting `/ballot/api/vote/`

## Ballot representation
```
{
    "id": 1,
    "title": "Elector's best contributor",
    "date_created": "2020-07-25T10:30:00Z",
    "deadline": "2020-09-25T23:59:59Z",
    "questions": [
        {
            "question_number": 0,
            "question_text": "Who is the best contrubitor to elector open source project?",
            "options": [
                {
                    "option_number": 0,
                    "option_text": "gdara17",
                    "votes": 17
                },
                {
                    "option_number": 1,
                    "option_text": "durid17",
                    "votes": 17
                }
            ]
        }
    ],
    "voter_list": [
        "voter1@example.com",
        "voter2@example.com",
        "voter3@example.com"
    ]
}
```

## Contributing
- Pull Requests are welcome!
- Feel free to open and discuss issues, ideas and possible feature implementations

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
