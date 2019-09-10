-- Deploy forum:message to pg

BEGIN;

CREATE TABLE forum.message (
	id SERIAL PRIMARY KEY,
	thread_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	text TEXT NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
	updated_at TIMESTAMP WITH TIME ZONE,

	FOREIGN KEY(thread_id) REFERENCES forum.thread(id) ON DELETE CASCADE,
	FOREIGN KEY(user_id) REFERENCES forum.user(id)
);

COMMIT;
