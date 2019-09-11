-- Revert forum:thread from sqlite

BEGIN;

DROP TABLE thread;

COMMIT;
