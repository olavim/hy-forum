-- Verify forum:thread on sqlite

BEGIN;

SELECT id, topic_id, user_id, title, created_at FROM "forum.thread" WHERE FALSE;

ROLLBACK;
