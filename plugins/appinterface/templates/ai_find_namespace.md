{% if namespaces is string %}
{{ namespaces }}
{% else %}
### Found {{ namespaces|length}} namespaces...
name | appname | cluster
---- | ------- | -------
{% for n in namespaces[:10] -%}
{{n['name']}} | {{n['app']['name']}} | {{n['cluster']['name']}}
{% endfor %}
{% if namespaces|length > 10 %}
More than 10 namespaces found. Please refine your search
{% endif %}
{% endif %}
