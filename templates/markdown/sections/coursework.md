{% extends "section.md" %}

{% block body %}
Some top-quality courses I've taken: <br>

{% for course in items %}
+ {{ course.name }}, {{ course.school}}, {{ course.semester }}
{% endfor %}
{% endblock body %}
