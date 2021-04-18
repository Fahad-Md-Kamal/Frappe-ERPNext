# A guide-line for frappe and ERPNext framework #

### Installation of Frappe framework and ERPNext on ubuntu 20.04 with python3 version ###
<br>

#### Prerequisite: ####
<hr>

* Python 3.6+
* Node.js 12
* Redis 5 &nbsp; &nbsp; &nbsp; &nbsp; (caching and real time updates)
* MariaDB 10.3.x / Postgres 9.5.x   &nbsp; &nbsp; &nbsp; &nbsp; (to run database driven apps)
* yarn 1.12+  &nbsp; &nbsp; &nbsp; &nbsp; (js dependency manager)
* pip 20+  &nbsp; &nbsp; &nbsp; &nbsp; (py dependency manager)
* wkhtmltopdf  &nbsp; &nbsp; &nbsp; &nbsp; (version 0.12.5 with patched qt)  (for pdf generation)
* cron  &nbsp; &nbsp; &nbsp; &nbsp; (bench's scheduled jobs: automated certificate renewal scheduled backups)

* NGINX  

<br>

### Create a Virtual Environment on the local machine’s desired directory.
<small> For my case, I’m going to create my project on Desktop’s subdirectory (ERPNext Folder). </small>
<br>
<br>

Open the terminal by pressing:
<kbd>CTL</kbd> + <kbd>ATL</kbd>+ <kbd>T</kbd>

Navigate into the Desktop by typing the command: 
> cd Desktop/

Create subfolder: 
> mkdir ERPNext

Install Virtual environment by: 
> sudo apt-get install python3-venv

Create python virtual environment: 
> python3 -m venv env

## Install Node Js:
<hr>

Install curl first: 
> sudo apt install curl

Download and execute the NodeSource installation script: 
> curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

This will:
* Add script of NodeSource signing key to your system, 
* Create an apt repository file, 
* Install all necessary packages and 
* Refresh the apt cache.

<br>
***If you need another Node.js version, for example 12.x, change the setup_14.x with setup_12.x***

<br>
<br>

Once the NodeSource repository is enabled, install Node.js and npm:
> sudo apt install nodejs

<br>

Check Node Version
> node --version

<br>

Check npm version
> npm --version

<br>

### Install yarn globally using node ###
> sudo npm install -g yarn

### Install git, python, and redis ###
> sudo apt install git python-dev redis-server


### Install MariaDB ###
> sudo apt-get install software-properties-common

<br>
<br>
<hr>

***If you are on Ubuntu version older than 20.04, run this before installing MariaDB:***
> apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8 add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.ubuntu-tw.org/mirror/mariadb/repo/10.3/ubuntu xenial main'

<hr>
<br>
<br>


***If you are on version Ubuntu 20.04, then MariaDB is available in default repo and you can directly run the below commands to install it***


> sudo apt-get update 

> sudo apt-get install mariadb-server-10.3
<hr>


<br>

***During this installation you'll be prompted to set the MySQL root password.***


<hr>
<strong>***N.B: If you are not prompted, you'll have to initialize the MySQL server setup yourself. You can do that by running the command.
(Remember: only run it if you're not prompted the password during setup.)
sudo mysql_secure_installation***</strong>
<hr>

<br>

***You will be prompted with the following commands during the process***

<hr>

>Enter current password for root (enter for none):
>> Change the root password? [Y/n] y
>> New password:
>> Re-enter new password:

> Remove anonymous users? [Y/n] y
> Disallow root login remotely? [Y/n] y
> Remove test database and access to it? [Y/n] y
> Reload privilege tables now? [Y/n] y

<br>
<br>
<hr>

***It is really important that you remember this password, since it'll be useful later on.***

<hr>
<br>
<br>

### You'll also need the MySQL database development files.
> sudo apt-get install libmysqlclient-dev

***Now, edit the MariaDB configuration file.***
> sudo nano /etc/mysql/my.cnf


<br>
<br>

***Add the following line to the end:***
<hr>

> [mysqld]
> innodb-file-format=barracuda

> innodb-file-per-table=1

> innodb-large-prefix=1

> character-set-client-handshake = FALSE

> character-set-server = utf8mb4
> collation-server = utf8mb4_unicode_ci

> [mysql]

> default-character-set = utf8mb4

<br>
<br>
<br>

<hr>
Restart MariaDB and enable it to automatically start at boot time.

> sudo systemctl restart mariadb

> sudo systemctl enable mariadb

Now, just restart the mysql service and and check status.
> sudo service mysql restart

> service mysql status


## Install wkhtmltopdf:
> sudo apt-get install xvfb libfontconfig wkhtmltopdf

<br>

(Activate the virtual environment with the command: source env/bin/activate)


<br>

## Install Nginx and Redis:
sudo apt -y install nginx redis-server

<br>

## Start Nginx and enable it to start at boot time.
> sudo systemctl start nginx

> sudo systemctl enable nginx

<br>

## Start Redis and enable it to start at boot time.
> sudo systemctl start redis-server

> sudo systemctl enable redis-server


<br>

## Install Frappe:

> pip3 install frappe-bench

<br>

***Confirm the bench installation by checking version***

> bench --version

<br>
<br>

## Create your first bench folder.
<hr>

> bench init frappe-bench

<br>
<br>

***While installing you might see some errors run the following command to install the dependency in order to avoid the error.***

> sudo apt-get install gcc python3-dev

<br>

***Create a new Frappe site.***

> bench new-site <site_name> --bd-name <site_database_name>

<br>
<br>

The above command will prompt you for the MySQL root password. Provide the password which you have set for the MySQL root user earlier. It will also ask you to set a new password for the administrator account. You will need this password later to log into the administrator dashboard.

<br>

***While creating the site you will be prompted to provide mysql password. If it prevents follow the following steps:***

<br>

**Database Login Issues**

In some cases Database may not login, to rectify the issue Please Follow below steps

> sudo nano /etc/mysql/my.cnf

Add the following lines at the end:
<br>

> [mysqld]

> skip-grant-tables

<br>

**Then Restart the service**

> sudo service mysql restart

<br>

***Login to Mysql & follow the command***
> mysql -u root

<br>
<hr>

> use mysql

> SELECT * FROM mysql.user WHERE user = 'root'; 

***(Look at the top to determine whether the password column is called password or authentication_string)***

> UPDATE mysql.user SET authentication_string = PASSWORD('123456’) where user = 'root' and host = 'localhost'; - Use the proper password column from above

> SELECT User, Host, plugin FROM user;

***(if Plugin is not mysql_native_password, then set the plugin by the below command)***

> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
> FLUSH PRIVILEGES;
> exit;

<br>

***
***
Remove the <strong>skip-grant-tables</strong> from <strong>/etc/mysql/my.cnf</strong> and restart the service & it's Done
***
***
<br>

### Now download ERPNext installation files from the remote git repository using Bench.
> bench get-app erpnext https://github.com/frappe/erpnext

<br>

### Install ERPNext on your newly created site.
> bench --site erp.testsite install-app erpnext

<br>
You can start the application immediately to check if the application installed successfully. 

> bench start

***

****You might face the error saying: Could not start up: Error in setup***

In such case:
* Make sure you didn't miss any dependencise.
* > cd /Desktop/frappe-bench

> sudo chown -R user:user *

***(For my case I’ve applied the following command since my user is mhfahad)***

>sudo chown -R mhfahad:mhfahad *

<br>

## Now start the app with the command:
***
> bench start

***

<br>
<br>
<br>

***
# Creating Custom Application for Frappe:

