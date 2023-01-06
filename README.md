# kib-hub
Django restframework API for house and offices listing

- Django restframework Web Api for taking land listing.

## Features
- Register,Login, and Logout a user
- Get all list of registered user
- Get all list of land owners and also be able to perform CRUD on land owners
- Get all list of land information and also perform CRUD on land information

## Requirements

- Python3.8.10
- Djanog 4.1
- Django restframework

## Set up and Installation
- Clone the repository
```bash
git clone https://github.com/Michael-Otieno/kib-hub/
```
 - Create and activate virtual environment
 ```bash
 python3 -m venv .venv - source .venv/bin/activate  
 ```
 - Install dependencies
  ```bash
pip install -r requirements.txt 
 ```
 - Run project
  ```bash
python3 manage.py runserver
 ```
 ## Structure
 | Endpoint | HTTP Method   | CRUD Method  | Result |
| :---:   | :---: | :---: |:---: |
| `register/` | POST   | CREATE  |Register a user |
| `login/` | POST  | POST |Login a user |
| `user/` | GET  | GET  |Get all users  |
| `logout/` | POST   | POST  |Update atendance detail  |
| `properties/` | GET  | GET |GET list of properties |
| `properties/` | POST  | CREATE |Add property |
| `properties/:id` | GET | GET |Get property information |
| `properties/:id` | PUT | UPDATE |Update property information |
| `properties/:id` | DELETE  | DELETE |Delete property |


## Use
- Use [Postman](https://www.postman.com/) for testing
 

## Contact Information
- If you have any question or contributions, please email me at m.otieno205@gmail.com

## License
- MIT Licence
- Copyright (c) 2022 Michael-Otieno

