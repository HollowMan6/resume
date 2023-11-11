{% extends "section.md" %}

{% block body %}
<table class="table table-hover">
{% for item in items.main %}
<tr>
  <td style='padding-right:0;'>
  <span class='cvdate'>{{ item.year }}</span>
  {% if item.url %}
     <a href="{{ item.url }}" target="_blank">{{ item.name }}</a>
  {% else %}
      {{item.name }}
  {% endif %}
  {% if item.details %}
  <br><p style="color:grey;font-size:1.4rem">{{ item.details }}</p>
  {% endif %}
  </td>
</tr>
{% endfor %}
</table>

### Reviewing
<table class="table table-hover">
{% for item in items.reviewing %}
<tr>
  <td style='padding-right:0;'>{{ item }}</td>
</tr>
{% endfor %}
</table>
{% endblock body %}
