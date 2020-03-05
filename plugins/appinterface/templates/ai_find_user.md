{% if users is string %}
{{ users }}
{% else %}
### Found {{ users|length}} users...

org_username | name | path
------------ | ---- | ----
{% for user in users %}{{ user['org_username'].ljust(7) }} | {{ user['name'] }} | {{ user['path'] }}
{% endfor %}
{% endif %}
