# Forum

> The Internet message board

A database application made as a part of practical work assignment.

---

Available at https://hy-forum.herokuapp.com/

# Description

A slightly modified version of the example topic "Keskustelufoorumi".

Aims to be a simplistic Internet message board, where users can create message threads inside a topic. A topic might be something like "Sports", while a message thread in said topic might discuss the Olympics.

# Testing locally

**1.** Run local setup script to initialize SQLite database and create environment configuration file.

```
$ ./scripts/local-setup.sh
```

**2.** Edit the environment configuration file to fit your needs. The file is named `.env` and is created during the setup script.

**3.** Install dependencies

```
$ pip install -r requirements.txt
```

**4.** Run the application

```
$ python run.py
```

# Documentation

- [Database Relationship Diagram](documentation/db-diagram.png)
- [User Stories](documentation/user-stories.md)