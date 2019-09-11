-- Deploy forum:message to sqlite

BEGIN;

CREATE TABLE message (
	id INTEGER PRIMARY KEY,
	thread_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	text TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP,

	FOREIGN KEY(thread_id) REFERENCES thread(id) ON DELETE CASCADE,
	FOREIGN KEY(user_id) REFERENCES user(id)
);

COMMIT;