-- Verify forum:thread on pg

BEGIN;

SELECT id, topic_id, user_id, title, created_at FROM forum.topic WHERE FALSE;

ROLLBACK;
