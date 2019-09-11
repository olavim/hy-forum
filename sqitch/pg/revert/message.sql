-- Revert forum:message from pg

BEGIN;

DROP TABLE forum.message;

COMMIT;
