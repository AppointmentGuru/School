{% if school_run_command|default(False) %}
{{school_run_command}}
{% else %}
gunicorn {{school_service}}.wsgi:application -b :{{school_port}} --reload
{% endif %}