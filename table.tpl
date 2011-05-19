{% extends base.tpl %}

{% block content %}
  <table>
    {% for r in rows %}
      <tr>
        <td>{% knum %}</td>
        <td>{% genomes %}</td>
        <td>{% genes %}</td>
      </tr>
    {% endfor %}
  </table>
{% endblock %}
