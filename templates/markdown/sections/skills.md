{% extends "section.md" %}

{% block body %}
<table class="table table-hover">
{% for item in items %}
<tr>
  <td class='col-md-2'><b>{{ item.title }}</b></td>
  <td>
{{ item.details }}
{% if item.sub_details %}
<br><p style="color:grey;font-size:1.4rem">{{ item.sub_details }}</p>
{% endif %}
  </td>
</tr>
{% endfor %}
</table>
{% endblock body %}
