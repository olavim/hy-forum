# Database schema

Below is listed the `CREATE TABLE` statements for each table, as they are defined for PostgreSQL.

## user

```sql
CREATE TABLE "user" (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE,
  password_hash VARCHAR(255),
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## role

```sql
CREATE TABLE role (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) UNIQUE,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## permission

```sql
CREATE TABLE permission (
  id SERIAL PRIMARY KEY,
  permission VARCHAR(255) UNIQUE,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## role_permission

```sql
CREATE TABLE role_permission (
  role_id INTEGER REFERENCES role(id) ON DELETE CASCADE,
  permission_id INTEGER REFERENCES permission(id) ON DELETE CASCADE,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (role_id, permission_id)
);
```

## role_membership

```sql
CREATE TABLE role_membership (
  role_id INTEGER REFERENCES role(id) ON DELETE CASCADE,
  user_id INTEGER REFERENCES user(id) ON DELETE CASCADE,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (role_id, user_id)
);
```

## topic

```sql
CREATE TABLE topic (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  description VARCHAR(255),
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## thread

```sql
CREATE TABLE thread (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  topic_id INTEGER REFERENCES topic(id) ON DELETE CASCADE,
  user_id INTEGER REFERENCES "user"(id) ON DELETE SET NULL,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## message

```sql
CREATE TABLE message (
  id SERIAL PRIMARY KEY,
  text TEXT,
  thread_id INTEGER REFERENCES thread(id) ON DELETE CASCADE,
  user_id INTEGER REFERENCES "user"(id) ON DELETE SET NULL,
  updated_by_id INTEGER REFERENCES "user"(id) ON DELETE SET NULL,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```