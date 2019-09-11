-- Revert forum:message from sqlite

BEGIN;

DROP TABLE message;

COMMIT;
