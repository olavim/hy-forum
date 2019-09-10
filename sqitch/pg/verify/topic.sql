-- Verify forum:topic on pg

BEGIN;

SELECT id, title, created_at FROM forum.topic WHERE FALSE;

ROLLBACK;
