-- Revert forum:topic from sqlite

BEGIN;

DROP TABLE "forum.topic";

COMMIT;
