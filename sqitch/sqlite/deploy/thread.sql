-- Deploy forum:thread to sqlite

BEGIN;

CREATE TABLE thread (
	id INTEGER PRIMARY KEY,
	topic_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	title VARCHAR(255) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP,

	FOREIGN KEY(topic_id) REFERENCES topic(id) ON DELETE CASCADE,
	FOREIGN KEY(user_id) REFERENCES user(id)
);

COMMIT;
