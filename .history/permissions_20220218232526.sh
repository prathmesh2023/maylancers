sudo ufw app info "Apache Full"

sudo ufw allow in "Apache Full"

sudo chown :www-data maylancer
sudo chown :www-data maylancer/db.sqlite3
sudo chown :www-data maylancer/satic/


sudo chown :www-data maylancer/media/



sudo chmod -R 775 maylancer/

sudo chmod -R 775 maylancer/db.sqlite3
sudo chmod -R 775 maylancer/satic/

sudo chmod -R 775 maylancer/media/


 sudo systemctl restart apache2