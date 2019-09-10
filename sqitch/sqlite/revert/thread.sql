-- Revert forum:thread from sqlite

BEGIN;

DROP TABLE "forum.thread";

COMMIT;
