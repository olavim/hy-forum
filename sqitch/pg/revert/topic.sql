-- Revert forum:topic from pg

BEGIN;

DROP TABLE forum.topic;

COMMIT;
