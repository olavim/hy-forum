# Forum

> The Internet message board

A database application made as a part of practical work assignment.

---

Available at https://hy-forum.herokuapp.com/

# Description

A slightly modified version of the example topic "Keskustelufoorumi".

Aims to be a simplistic Internet message board, where users can create message threads inside a topic. A topic might be something like "Sports", while a message thread in said topic might discuss the Olympics.

# Testing locally

**1.** Rename the environment configuration file and edit it to fit your needs.

```
$ cp .env.dist .env
```

**2.** Install dependencies

```
$ pip install -r requirements.txt
```

**3.** Run the application

```
$ python run.py
```

# Database migrations

The project uses [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) for database migrations.

Migrations are run automatically when you run the application.

To see available CLI commands, run

```
$ python run.py db --help
```

# Documentation

- [Database Relationship Diagram (Final)](documentation/db-diagram.png)
- [Database Relationship Diagram (Current)](documentation/db-diagram-current.png)
- [User Stories](documentation/user-stories.md)

## For the reviewer

[Register](https://hy-forum.herokuapp.com/register) as a new user and you can fiddle around as much as you want.

You can alternatively [login](https://hy-forum.herokuapp.com/login) as the test user:
- Username: test
- Password: 1234
