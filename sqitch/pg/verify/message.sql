-- Verify forum:message on pg

BEGIN;

SELECT id, thread_id, user_id, text, created_at FROM forum.message WHERE FALSE;

ROLLBACK;
