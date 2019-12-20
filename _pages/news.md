---
---

# News

{% for post in site.posts %}
{% if post.display %}

{{ post.excerpt }}

Posted on {{ post.date | date_to_long_string }} by {{ post.author }}.

{% if post.excerpt != post.content %}
<a href="{{ site.baseurl }}{{ post.url }}">Read more</a>
{% endif %}

{% endif %}
{% endfor %}
