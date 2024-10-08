CREATE USER 'contact_user'@'localhost' IDENTIFIED BY '1688Contacts';
GRANT ALL PRIVILEGES ON contact_db.* TO 'contact_user'@'%';
FLUSH PRIVILEGES;
