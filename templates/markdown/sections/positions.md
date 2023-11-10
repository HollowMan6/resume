{% extends "section.md" %}

{% block body %}
<table class="table table-hover">
{% for i in items %}
<tr>
  <td style='padding-right:0;'>
<span class='cvdate'>{{ i.dates }}</span>
<p markdown="1" style='margin: 0'>
{%- if i.title -%}
<strong>{{ i.title }}</strong>, <em>{{ i.place }}</em>
{%- else -%}
<strong>{{ i.place}}</strong>
{%- endif -%}
{% if i.location %}
, {{ i.location }}
{% endif %}
{% if i.inline_detail %}
<span markdown="1" style="color:grey;font-size:1.4rem;margin: 0">
({{ i.inline_detail }})
</span>
{%- endif -%}
</p>
{% if i.details %}
  <p style='margin-top:-1em;margin-bottom:0em' markdown='1'>
  {% for detail in i.details %}
  <br> • {{ detail }}
  {% endfor %}
  </p>
{% endif %}
  </td>
</tr>
{% endfor %}
</table>
{% endblock body %}
