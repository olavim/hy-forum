# User stories

- [x] As a guest, I can list existing topics, threads, and messages.
  ```sql
  SELECT * FROM topic;
  ```
  ```sql
  SELECT * FROM thread WHERE topic_id = ?;
  ```
  ```sql
  SELECT * FROM message WHERE thread_id = ?;
  ```
- [x] As a guest, I can search for threads by their title.
  ```sql
  SELECT * FROM thread WHERE title LIKE '%?%';
  ```
- [x] As a guest, I can search for messages by their content.
  ```sql
  SELECT * FROM message WHERE text LIKE '%?%';
  ```
- [x] As a user, I can post new messages to threads.
  ```sql
  INSERT INTO message (text, thread_id, user_id) VALUES (?, ?, ?);
  ```
- [x] As a user, I can edit and delete my own messages.
  ```sql
  UPDATE message SET text = ? WHERE id = ?;
  ```
  ```sql
  DELETE FROM message WHERE id = ?;
  ```
- [x] As a user, I can create new threads with a given title.
  ```sql
  INSERT INTO thread (title, topic_id, user_id) VALUES (?, ?, ?);
  ```
- [x] As a moderator, I can edit and delete messages of other users.
  ```sql
  UPDATE message SET text = ? WHERE id = ?;
  ```
  ```sql
  DELETE FROM message WHERE id = ?;
  ```
- [x] As a moderator, I can edit the title of, and delete threads created by any user.
  ```sql
  UPDATE thread SET title = ? WHERE id = ?;
  ```
  ```sql
  DELETE FROM thread WHERE id = ?;
  ```
- [x] As a moderator, I can create new topics with a given title and description.
  ```sql
  INSERT INTO topic (title, description) VALUES (?, ?);
  ```
- [x] As a moderator, I can edit the title and description of, and delete existing topics.
  ```sql
  UPDATE topic SET title = ?, description = ? WHERE id = ?;
  ```
  ```sql
  DELETE FROM topic WHERE id = ?;
  ```
- [x] As an administrator, I can create new roles. Users who have said roles will gain privileges according to their configuration.
  ```sql
  INSERT INTO role (name) VALUES (?);
  ```
  ```sql
  INSERT INTO role_permission (role_id, permission_id) VALUES (?, ?);
  ```
- [x] As an administrator, I can give an existing role to a user.
  ```sql
  INSERT INTO role_membership (role_id, user_id) VALUES (?, ?);
  ```

### Terminology

- **Guest**: A person who has _not_ logged in.
- **User**: A person who _has_ logged in.
- **Moderator**: A user with heightened privileges. Flexible term used to signify users who have any, _but not all_, special privileges; different moderators might have different privileges.
- **Administrator**: A user with all privileges, most notably group management.