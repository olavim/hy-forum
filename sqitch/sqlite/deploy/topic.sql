-- Deploy forum:topic to sqlite

BEGIN;

CREATE TABLE "forum.topic" (
	id INTEGER PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP
);

COMMIT;
