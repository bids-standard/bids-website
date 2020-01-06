---
---

# News

{% for post in site.posts %}
{% if post.display %}

{{ post.excerpt }}

{% if post.excerpt != post.content %}
  <a href="{{ post.url | relative_url }}">Read more ...</a>
{% else %}
  <a href="{{ post.url | relative_url }}">Link to this post ...</a>
{% endif %}

<em>Posted on {{ post.date | date_to_long_string }}{% if post.author %} by {{ post.author }}{% endif %}.</em>

{% endif %}
{% endfor %}
