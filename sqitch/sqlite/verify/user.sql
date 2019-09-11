-- Verify forum:user on sqlite

BEGIN;

SELECT id, username, password_hash, created_at FROM user WHERE FALSE;

ROLLBACK;
