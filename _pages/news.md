---
---

# News

{% for post in site.posts %}
{% if post.display %}

{{ post.excerpt }}

{% capture content_words %}{{ post.content | strip_html | number_of_words }}{% endcapture %}
{% capture excerpt_words %}{{ post.excerpt | strip_html | number_of_words }}{% endcapture %}
{% if content_words != excerpt_words %}
<a href="{{ post.url | relative_url }}">Read more ...</a>
{% endif %}

<em>Posted on {{ post.date | date_to_long_string }}{% if post.author %} by {{ post.author }}{% endif %}.</em>

{% endif %}
{% endfor %}
