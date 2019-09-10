-- Deploy forum:thread to pg

BEGIN;

CREATE TABLE forum.thread (
	id SERIAL PRIMARY KEY,
	topic_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	title VARCHAR(255) NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
	updated_at TIMESTAMP WITH TIME ZONE,

	FOREIGN KEY(topic_id) REFERENCES forum.topic(id) ON DELETE CASCADE,
	FOREIGN KEY(user_id) REFERENCES forum.user(id)
);

COMMIT;
