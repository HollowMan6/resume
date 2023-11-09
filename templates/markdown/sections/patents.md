{% extends "section.md" %}

{% block body %}
{% for item in items %}
+ {{ item.name }}, <a href="{{ item.url }}">{{ item.id }}</a>
{% endfor %}
{% endblock body %}
