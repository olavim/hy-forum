-- Deploy forum:topic to pg

BEGIN;

CREATE TABLE forum.topic (
	id SERIAL PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
	updated_at TIMESTAMP WITH TIME ZONE
);

COMMIT;
