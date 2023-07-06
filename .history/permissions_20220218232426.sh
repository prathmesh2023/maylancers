sudo ufw app info "Apache Full"

sudo ufw allow in "Apache Full"

sudo chown :www-data maylancer
sudo chown :www-data vdf/db.sqlite3
sudo chown :www-data vdf/satic/
sudo chown :www-data vdf/satic/admin/

sudo chown :www-data vdf/media/
sudo chown :www-data vdf/media/app1/gallery/imgs/

sudo chown :www-data vdf/media/app1/mediafiles/imgs/

sudo chown :www-data vdf/media/images/mou/logo

sudo chmod -R 775 vdf/

sudo chmod -R 775 vdf/db.sqlite3
sudo chmod -R 775 vdf/satic/
sudo chmod -R 775 vdf/satic/admin/
sudo chmod -R 775 vdf/media/
sudo chmod -R 775 vdf/media/app1/gallery/imgs/
sudo chmod -R 775 vdf/media/app1/mediafiles/imgs/

 sudo chmod -R 775 vdf/media/images/mou/logo

 sudo systemctl restart apache2