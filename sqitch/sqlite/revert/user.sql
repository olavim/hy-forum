-- Revert forum:user from sqlite

BEGIN;

DROP TABLE user;

COMMIT;
