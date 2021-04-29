# Adding JavaScript File

***If JavaScript file is not adding to the desired template automatically than:***

* Create www folder in public folder. add another folder callded js and place the js file in that particular folder.
* Now go to the base template folder (that is being inherited by other web portal pages of your site) add script block of jinja template.
* Now go to your desired template where you are extending the base and add jinja script block.
* Inside jinja block add html script tag and add source with the location of your site's asset folder.