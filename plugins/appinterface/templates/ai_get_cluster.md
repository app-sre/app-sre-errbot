{% if cluster is string %}
{{ cluster }}
{% else %}
### {{ cluster['name'] }}

key | value
--- | -----
{% for key, value in cluster.items() %}{% if key and value and value is string %}{{key}} | {{value}}{% endif %}
{% endfor %}
{% endif %}
