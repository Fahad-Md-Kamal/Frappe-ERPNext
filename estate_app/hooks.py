# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from .routes import urlpatterns
from .jinja import jenvs

app_name = "estate_app"
app_title = "Estate App"
app_publisher = "Fahad Md Kamal"
app_description = "Development Section"
app_icon = "octicon-container-24"
app_color = "#adaada"
app_email = "faahad.hossain@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/estate_app/homeland/icon-brain-blue.png"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/estate_app/css/estate_app.css"
# app_include_js = "/assets/estate_app/js/estate_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/estate_app/css/estate_app.css"
# web_include_js = "/assets/estate_app/js/estate_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "estate_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Expense Claim" : "public/js/doctype_plugin/expense_claim.js",
	}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website route generator
website_route_rules = urlpatterns

jinja = jenvs


# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "estate_app.install.before_install"
# after_install = "estate_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "estate_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
	"Property":{
		# Controller_Event : Scripting location
		"before_save": "estate_app.estate_app.doctype.property.events.validate",
		"on_update": "estate_app.estate_app.doctype.property.events.on_update",
		"after_insert": "estate_app.estate_app.doctype.property.events.after_insert",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"estate_app.tasks.all"
# 	],
# 	"daily": [
# 		"estate_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"estate_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"estate_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"estate_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "estate_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "estate_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "estate_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

