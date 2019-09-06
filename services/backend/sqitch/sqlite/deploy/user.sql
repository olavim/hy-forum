-- Deploy forum:user to sqlite

BEGIN;

CREATE TABLE "forum.user" (
	id INTEGER PRIMARY KEY,
	username VARCHAR(255) NOT NULL,
	password VARCHAR(80) NOT NULL,
	password_salt VARCHAR(80) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	updated_at TIMESTAMP NULL
);

COMMIT;
