-- Revert forum:message from sqlite

BEGIN;

DROP TABLE "forum.message";

COMMIT;
