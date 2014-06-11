${request.context}
<ul>
%for container in request.context:
<li>${container}</li>
%endfor
</ul>