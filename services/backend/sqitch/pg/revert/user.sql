-- Revert forum:user from pg

BEGIN;

DROP TABLE forum.user;

COMMIT;
