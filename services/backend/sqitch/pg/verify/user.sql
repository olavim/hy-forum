-- Verify forum:user on pg

BEGIN;

SELECT id, username, password, password_salt, created_at FROM forum.user WHERE FALSE;

ROLLBACK;
