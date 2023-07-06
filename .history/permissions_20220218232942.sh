sudo ufw app info "Apache Full"

sudo ufw allow in "Apache Full"

sudo chown :www-data maylancer
sudo chown :www-data maylancer/db.sqlite3
sudo chown :www-data maylancer/satic/
sudo chown :www-data maylancer/satic/bootstrap-5/
sudo chown :www-data maylancer/satic/css/
sudo chown :www-data maylancer/satic/img





sudo chown :www-data maylancer/media/
sudo chown :www-data maylancer/media/app1/img/category
sudo chown :www-data maylancer/media/app1/img/post/thumb
sudo chown :www-data maylancer/media/app1/img/dp



sudo chmod -R 775 maylancer/

sudo chmod -R 775 maylancer/db.sqlite3
sudo chmod -R 775 maylancer/satic/
sudo chmod -R 775 maylancer/satic/bootstrap-5/
sudo chmod -R 775 maylancer/satic/css/
sudo chmod -R 775 maylancer/satic/img/



sudo chmod -R 775 maylancer/media/
sudo chmod -R 775 maylancer/media/app1/img/category
sudo chmod -R 775 maylancer/media/app1/img/post/thumb
sudo chmod -R 775 maylancer/media/app1/img/dp


 sudo systemctl restart apache2

 


 

 