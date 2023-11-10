{% extends "section.md" %}

{% block body %}
Some top-quality courses I've taken: <br>

<table class="table table-hover">
    {% for course in items %}
    <tr>
        <td class='col-md-2'><b>{{ course.name }}</b>, <i>{{ course.school}}</i></td>
        <td class='col-md-2' style='text-align:right;'>{{ course.semester }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock body %}
