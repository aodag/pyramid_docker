${request.context}
<ul>
%for container in request.context:
<li><a href="${request.resource_url(container)}">${container}</a></li>
%endfor
</ul>