-- Revert forum:topic from sqlite

BEGIN;

DROP TABLE topic;

COMMIT;
