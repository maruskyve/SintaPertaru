SHOW DATABASES;
USE sinta_pertaru;

# SELECT
SELECT * FROM app_employee;
SELECT * FROM app_user;
SELECT * FROM app_landdata;

# SELECT WITH FILTER
SELECT COUNT(*) FROM app_landdata;
SELECT * FROM app_landdata WHERE land_data_suitability IS NOT NULL AND land_data_type='test';
