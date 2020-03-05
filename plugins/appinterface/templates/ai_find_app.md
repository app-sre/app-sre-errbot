{% if apps is string %}
{{ apps }}
{% else %}
### Found {{ apps|length}} apps...
name | serviceOwners
---- | -------------
{% for a in apps[:10] -%}
{{a['name']}} | {% for o in a['serviceOwners'] %}{{o['name']}}{% if not loop.last %}, {% endif %}{% endfor %}
{% endfor %}
{% if apps|length > 10 %}
More than 10 apps found. Please refine your search
{% endif %}
{% endif %}
