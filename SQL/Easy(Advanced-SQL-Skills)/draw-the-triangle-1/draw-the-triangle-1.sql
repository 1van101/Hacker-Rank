SET @P = 20;             
SELECT REPEAT('* ', @P := @P - 1) 
FROM information_schema.tables
LIMIT 20;