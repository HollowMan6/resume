{% extends "section.md" %}

{% block body %}
{{ followers }} GitHub followers.
{{ total_stars }} GitHub stars across all of the following selected repositories:

<table class="table table-hover">
{% for item in items %}
<tr>
  <td align='right' style='padding-right:0;padding-left:0;'>{{ loop.index }}.</td>
  <td>
    <span class='cvdate'>{{ item.year }}</span>
    <a href="{{ item.repo_url }}" target="_blank">{{ item.name }}</a> |
    <i class="fa fas fa-star"></i> {{ item.stars }} |
    <em>{{ item.desc }}</em>
    {% if item.rank %}
    <br><p style="color:grey;font-size:1.4rem">Rank #{{ item.rank }} among all contributors with {{ item.commits }} commits, {{ item.additons }} lines of additions and {{ item.deletions }} lines of deletions</p>
    {% endif %}
  </td>
</tr>
{% endfor %}
</table>
{% endblock body %}
