sudo ufw app info "Apache Full"

sudo ufw allow in "Apache Full"

sudo chown :www-data maylancer
sudo chown :www-data maylancer/db.sqlite3
sudo chown :www-data maylancer/static/
sudo chown :www-data maylancer/static/bootstrap-5/
sudo chown :www-data maylancer/static/css/
sudo chown :www-data maylancer/static/img





sudo chown :www-data maylancer/media/
sudo chown :www-data maylancer/media/app1/img/category
sudo chown :www-data maylancer/media/app1/img/post/thumb
sudo chown :www-data maylancer/media/app1/img/dp



sudo chmod -R 775 maylancer/

sudo chmod -R 775 maylancer/db.sqlite3
sudo chmod -R 775 maylancer/static/
sudo chmod -R 775 maylancer/static/bootstrap-5/
sudo chmod -R 775 maylancer/static/css/
sudo chmod -R 775 maylancer/static/img/



sudo chmod -R 775 maylancer/media/
sudo chmod -R 775 maylancer/media/app1/img/category
sudo chmod -R 775 maylancer/media/app1/img/post/thumb
sudo chmod -R 775 maylancer/media/app1/img/dp


 sudo systemctl restart apache2

 


 

 