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

![100002010000032D0000012B6AB89DD1260CD9C2](https://user-images.githubusercontent.com/34704464/115140638-1123ed00-a05a-11eb-94bd-305645c87a7f.png)


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

***If you need another Node.js version, for example 12.x, change the setup_14.x with setup_12.x***

![10000201000004680000023975178A769CA9C0C3](https://user-images.githubusercontent.com/34704464/115140671-429cb880-a05a-11eb-9616-2c0c4b2e752e.png)


Once the NodeSource repository is enabled, install Node.js and npm:
> sudo apt install nodejs

<br>

Check Node Version
> node --version

<br>

Check npm version
> npm --version


![10000201000004680000023978A0A5CF4B94B19A](https://user-images.githubusercontent.com/34704464/115140695-6c55df80-a05a-11eb-8c96-35151a52340e.png)


### Install yarn globally using node ###
> sudo npm install -g yarn

![10000201000004830000011909DADA1F43927846](https://user-images.githubusercontent.com/34704464/115140721-8c859e80-a05a-11eb-8c4e-4a352545ebdc.png)

### Install git, python, and redis ###
> sudo apt install git python-dev redis-server


![100002010000046800000239D17A35A35AB20CDB](https://user-images.githubusercontent.com/34704464/115140746-a7581300-a05a-11eb-8b46-55c5c509e802.png)


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


![1000020100000468000001DF171A126A852456B9](https://user-images.githubusercontent.com/34704464/115140766-c787d200-a05a-11eb-82f9-90146d1f95da.png)

<hr>

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


![100002010000045600000227B0C40BBBE88F5152](https://user-images.githubusercontent.com/34704464/115141003-f94d6880-a05b-11eb-877b-95eed4e1a60c.png)
![1000020100000456000002271EA24C79B6C9BC36](https://user-images.githubusercontent.com/34704464/115140984-dcb13080-a05b-11eb-8289-0fc1341b745a.png)
![100002010000045600000227570FD58ACDCA0E2F](https://user-images.githubusercontent.com/34704464/115141067-4598a880-a05c-11eb-91c7-058f25758b1d.png)

<hr>

***It is really important that you remember this password, since it'll be useful later on.***

<hr>
<br>
<br>

### You'll also need the MySQL database development files.
> sudo apt-get install libmysqlclient-dev


![1000020100000456000002274338C021506DA343](https://user-images.githubusercontent.com/34704464/115141097-6660fe00-a05c-11eb-990e-4ed6fc7b25cf.png)

<br>

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


![1000020100000456000002813505EB54324D2094](https://user-images.githubusercontent.com/34704464/115141126-88f31700-a05c-11eb-9488-f4dc59b400d1.png)


<hr>
Restart MariaDB and enable it to automatically start at boot time.

> sudo systemctl restart mariadb

> sudo systemctl enable mariadb

Now, just restart the mysql service and and check status.
> sudo service mysql restart

> service mysql status


![1000020100000456000002814561C2EC7A41157B](https://user-images.githubusercontent.com/34704464/115141166-bc35a600-a05c-11eb-96a4-f13c89c3fc14.png)

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

![10000201000005FD000001CD0FDE34F3CC332ED2](https://user-images.githubusercontent.com/34704464/115141278-28180e80-a05d-11eb-8cff-96575dbf0220.png)
![1000020100000363000002C91928EAB6FBC66FD9](https://user-images.githubusercontent.com/34704464/115141307-51389f00-a05d-11eb-835c-c9265c34b73f.png)

***While installing you might see some errors run the following command to install the dependency in order to avoid the error.***

> sudo apt-get install gcc python3-dev

<br>

***Create a new Frappe site.***

> bench new-site <site_name> --bd-name <site_database_name>

<br>
<br>

The above command will prompt you for the MySQL root password. Provide the password which you have set for the MySQL root user earlier. It will also ask you to set a new password for the administrator account. You will need this password later to log into the administrator dashboard.

![10000201000004F80000015436722D45B2D09340](https://user-images.githubusercontent.com/34704464/115141330-6b727d00-a05d-11eb-8184-e2d0aaefacb4.png)

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

![10000201000004F80000021A8F54FBEFDC0F7D86](https://user-images.githubusercontent.com/34704464/115141388-c2785200-a05d-11eb-8c2e-180c40be5abc.png)


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

![10000201000004F8000001F60A62D5F2F1D54C59](https://user-images.githubusercontent.com/34704464/115141420-ea67b580-a05d-11eb-9918-c484917f7358.png)

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

**Creating a custom Module**
<small> Here I'm going to create a module named Alesha Products
</small>
<br>

### Creating the Module / app
<br>

Navigate to the project
> bench new-app alesha_product

***This will ask you app specific information along with some default values***

Once the installation is complete, you will have to install the app to the site. By default the site doesn't know the app details.

<br>

In order to install the application to the site you need to apply the following command.
> bench --site <site_name> install-app <app_or_module_name>

In order to check installed apps of a particular site:
> bench --site <site_name> list-apps

***There are several site commands. To see all site commands.***
> bench --site <site_name> --help

The custom app/module is available in the site. Now we have to create doctype for the application to use.

In order to customize the site we need to run the site with enabled developer mode.
To do that type:
> bench --site <site_name> set-config --global developer_mode 1

<br>
<br>

## DocType
***
In simple, DocType is the database table name of Frappe Framework.
You will be directly interecting with database tabels using Frappe's DocType.

<br>

In our custom app/ module we will create two doctypes.
1. Vendors
2. Alesha Products

<br>

### Creating DocType
***
While in Desk, type "doctype" in the search bar and select the DocType List option. You will be navigated to the DocType list where you will see a bunch of DocTypes. These are the DocTypes that are bundled with the framework.

***The first doctype we will create is Vendors.***
***

To create it, click on New.
1. Enter Name as Alesha Vendors.
2. Select Library Management in Module
3. Add the following fields in the Fields table:

    > Image(Attach Image)

    > Full Name (Data)
    
    > Eamil (Data)
    
    > Contact (Text Editor)
    
    > Address (Data)
    
    > Bank Name (data)
    
    > Bank Account Name (data)
    
    > Bank Account Number (data)
    
    > Route (data)
    
    > Vendor Type (Select) Enter options: Shop and Company (Type Shop, hit enter, then Type Company)

4. To save the form, Click save button
5. add the following text to the auto naming field in the bottom so that the vendor name is unique throughout the list.

    ALM.VEN.#####

6. In Form Settings section add the insert image to the text box. This lets frappe know which field of the table is image field so that it can handle that field in such way.

7. In View Settings section, add which form field name you want to name the html view title name

    <small>**For my purpose I've used full_name field**</small>

8. You can also restict the permission to different user roles from the Permission Rules section. 

    <small>**Here I've added Business Developer who has the permission to read, write, create and delete permission. On the contrary, Operations role will have only read permission.**</small>

9. Now save again. Reload the page by selecting Reload option from three dot button beside the save button.

10. Go to vendor List
11. Create Vendor


You will see that vandor with your given information has shown in the vendor list.

***By Checking the Database You can also see new database table of named 'tabVendor'***

### Now Let's customize the Form look.

1. Add row to vendor form fields table.
2. Make the type Coumn Break
3. Drag it to middle of the fields table rows.
4. Save changes. 
5. Now go to add new vendor. You will see the long for is now splitted into two columns.
6. We can also seperate a section of form to new sectin. In that case we have to add another row to the table as set the type Section Break
7. Than drag the row before the row where you want to break the section.


<br>
<hr>
<br>

## Now Add Let's Add the Product DocType to our custom DocType
***

1. Go to Doctype List.
2. press <kbd> + add DocType </kbd>  blue Button
3. Enter Doctype Name
4. Add Module Name
5. Check Is Submittable Below Module selection text input.
(This add three events to the form to save it)
6. Add desired fields
7. Modify Naming, Form Settings, View Settings, Permission Rules
8. Save the form

### Adding Web View for the Product ###
1. Check the "Has Web View", Allow Guest to View, 
Index Web Pages for Search
2. Add your DocType name into the Route input field e.g. Mart Product as mart_product.
3. Add a new row to the Form Fields table named Route
4. Make the field Hidden from row edit menu since it will be auto generated.
5. Save Changes.

## Adding Custom Module to Our admin deshboard with outher module list.

1. Type workspace at searchbox and navigate to the Workspace List.
2. press the <kbd> + Add Workspace </kbd> button.
3. Enter your Module Name that you want to call within the site.
4. Select the Module for the Module list
5. Select Category
6. Enter Icon name that you want to represent your app or leave blank
7. leave Onboarding blank
8. check Is Standared from the right section
9. Give Dashboards sectionlabel a name and add chart to teh charts row.
10. Add Module specific all doctypes to the shortcut section and link them (The System will suggest all of the names, No need to memorise or else.)
11. Add Link Cards similarly.
12. Save and reload.
13. Now go to the admin home page.
14. Make a Hard Refreash or press <kbd>CTL</kbd> + <kbd>SHIFT</kbd> + <kbd> R </kbd>

You can see your Custom Module at the Left side of all module lists with your Given name and Icon along with
