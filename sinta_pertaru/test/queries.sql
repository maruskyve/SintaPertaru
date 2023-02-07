SHOW DATABASES;
USE sinta_pertaru;

# DESCRIBES
DESCRIBE app_employee;
DESCRIBE app_user;
DESCRIBE app_landdata;

# SELECTS
SELECT * FROM app_employee;
SELECT * FROM app_user;
SELECT * FROM app_landdata;

# SELECTS WITH FILTER
SELECT COUNT(*) FROM app_employee;
SELECT COUNT(*) FROM app_user;
SELECT COUNT(*) FROM app_landdata;
SELECT * FROM app_landdata WHERE land_data_suitability IS NOT NULL AND land_data_type='test';

# INSERTS
INSERT INTO app_employee (employee_id, employee_name, employee_class, employee_gender, employee_address, employee_phone_number, employee_date_of_birth, employee_birth_district)
    VALUES (118475748392734545, 'Dedy Pamungkas', 'Penata Muda Tk.I Gol III/b', 'male', 'Pedak, Sinduharjo, Kec. Ngaglik, Kabupaten Sleman, Daerah Istimewa Yogyakarta', '+6284785739584', '1991-05-03', 'Sleman');
INSERT INTO app_employee (employee_id, employee_name, employee_class, employee_gender, employee_address, employee_phone_number, employee_date_of_birth, employee_birth_district)
    VALUES (198475748392734532, 'Rosiyah', 'Penata Gol III/c', 'female', 'Warak Kidul, Sumberadi, Kec. Mlati, Kabupaten Sleman, Daerah Istimewa Yogyakarta', '+6284637564967', '1968-06-11', 'Sleman');
INSERT INTO app_employee (employee_id, employee_name, employee_class, employee_gender, employee_address, employee_phone_number, employee_date_of_birth, employee_birth_district)
    VALUES (184758397489684456, 'Heru Suyito', 'Penata Muda Gol III/a', 'male', 'Wonorejo, Sariharjo, Kec. Ngaglik, Kabupaten Sleman, Daerah Istimewa Yogyakarta', '+6287463778564', '1973-01-07', 'Sleman');
