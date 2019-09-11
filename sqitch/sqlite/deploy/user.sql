-- Deploy forum:user to sqlite

BEGIN;

CREATE TABLE user (
	id INTEGER PRIMARY KEY,
	username VARCHAR(255) NOT NULL,
	password_hash VARCHAR(255) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP
);

COMMIT;
