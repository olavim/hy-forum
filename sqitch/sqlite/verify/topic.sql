-- Verify forum:topic on sqlite

BEGIN;

SELECT id, title, created_at FROM topic WHERE FALSE;

ROLLBACK;
