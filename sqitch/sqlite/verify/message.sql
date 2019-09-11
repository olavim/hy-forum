-- Verify forum:message on sqlite

BEGIN;

SELECT id, thread_id, user_id, text, created_at FROM message WHERE FALSE;

ROLLBACK;
