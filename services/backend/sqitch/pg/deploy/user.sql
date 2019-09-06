-- Deploy forum:user to pg

BEGIN;

CREATE TABLE forum.user (
	id SERIAL PRIMARY KEY,
	username VARCHAR(255) NOT NULL,
	password VARCHAR(80) NOT NULL,
	password_salt VARCHAR(80) NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
	updated_at TIMESTAMP WITH TIME ZONE NULL
);

COMMIT;
