{% extends "section.md" %}

{% block body %}
<table class="table table-hover">
{% for i in items %}
<tr>
  <td>
<p markdown="1" style='margin: 0'>
{% if i.title %}
<strong>{{ i.title }}</strong>, {{ i.place }}
{% else %}
<strong>{{ i.place}}</strong>,
{% endif %}
{{ i.location }}
{% if i.details %}
<ul>
{% for detail in i.details %}
<li>{{ detail }}</li>
{% endfor %}
</ul>
{% endif %}
</p>
  </td>
  <td class='col-md-2' style='text-align:right;'>{{ i.dates }}</td>
</tr>
{% endfor %}
</table>
{% endblock body %}
