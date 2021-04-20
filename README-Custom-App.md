# Create & Install New app

### Create your desired app
> bench new-app estate_app


### Install the created app to the site for customization.
> bench --site bigtech install-app estate_app


***
## Enable Developer mode otherwise you won't be able to customize the site:
> bench --site <site_name> set-config developer_mode 1

This will add following code to the sites/bigtech/site_config.json file:

```
{
 "db_name": "<database_name>",
 "db_password": "<password_hash>",
 "db_type": "mariadb",
 "developer_mode": 1
}
```

## Adding DocType to the app
* Type DocType in serach box
* Press Add DocType
* Give Doctype Name, Module name which it belongs
* Uncheck the Custom Checkbox if checked
* Add DocType fields from row
* Press Save

(for better understanding visit: https://frappeframework.com/docs/user/en/tutorial/create-a-doctype)

<br>

This will create new file to your custom app directory called doctype.

