{% if clusters is string %}
{{ clusters }}
{% else %}
### Found {{ clusters|length}} clusters...
name | consoleUrl | internal
---- | ---------- | --------
{% for c in clusters[:10] -%}
{{c['name']}} | {{c['consoleUrl']}} | {{c['internal']}} 
{% endfor %}
{% if clusters|length > 10 %}
More than 10 clusters found. Please refine your search
{% endif %}
{% endif %}
