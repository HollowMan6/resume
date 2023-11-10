{% extends "section.md" %}

{% block body %}
<table class="table table-hover">
    {% for item in items %}
    <tr>
        <td class='col-md-2'>{{ item.name }}</td>
        <td class='col-md-2' style='text-align:right;'>
            <a href="{{ item.url }}" target="_blank">{{ item.id }}</a>
        </td>
    </tr>
    {% endfor %}
</table>
{% endblock body %}
