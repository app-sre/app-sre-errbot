{% if user is string %}
{{ user }}
{% else %}
### {{ user['org_username'] }}

key | value
--- | -----
{% for key, value in user.items() %}{{key}} | {{value}}
{% endfor %}
{% endif %}
