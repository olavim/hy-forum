-- Revert forum:init from pg

BEGIN;

DROP SCHEMA forum;

COMMIT;
