-- Revert forum:thread from pg

BEGIN;

DROP TABLE forum.thread;

COMMIT;
