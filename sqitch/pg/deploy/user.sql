-- Deploy forum:user to pg

BEGIN;

CREATE TABLE forum.user (
	id SERIAL PRIMARY KEY,
	username VARCHAR(255) NOT NULL,
	password_hash VARCHAR(255) NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
	updated_at TIMESTAMP WITH TIME ZONE
);

COMMIT;
