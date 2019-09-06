-- Revert forum:user from sqlite

BEGIN;

DROP TABLE "forum.user";

COMMIT;
