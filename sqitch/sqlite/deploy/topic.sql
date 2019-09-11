-- Deploy forum:topic to sqlite

BEGIN;

CREATE TABLE topic (
	id INTEGER PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
	updated_at TIMESTAMP
);

COMMIT;
