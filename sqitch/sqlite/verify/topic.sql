-- Verify forum:topic on sqlite

BEGIN;

SELECT id, title, created_at FROM "forum.topic" WHERE FALSE;

ROLLBACK;
