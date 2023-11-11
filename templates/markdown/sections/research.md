{% extends "section.md" %}

{% block body %}
<table class="table table-hover">
{% for r in items %}
<tr>
  <td class='col-md-3'>{{ r.dates }}</td>
  <td>
    <strong>{{ r.name }}</strong> <br> {{ r.advisor }}, <i>{{ r.place }}</i>
  </td>
</tr>
{% endfor %}
</table>

{% endblock body %}
