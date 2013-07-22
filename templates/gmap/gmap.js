function initialize() {
	var mapOptions = {
		zoom: 13,
		center: new google.maps.LatLng(23.37, 116.71),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	var map = new google.maps.Map(document.getElementById('map-canvas'),
				      mapOptions);

	addMarker(map);
}

function loadScript() {
	var script = document.createElement('script');
	script.type = 'text/javascript';
	script.src = '{{ GOOGLE_MAPS_API_URL }}?key={{ GOOGLE_MAPS_API_KEY }}&language=zh-CN&sensor=false&' +
		'callback=initialize';
	document.body.appendChild(script);
}

function addMarker(map) {
	var position, maker;
	var infowindow = new google.maps.InfoWindow();

	{% for point in points %}
	position = new google.maps.LatLng(
		{{ point.latitude }},
		{{ point.longitude }});
	marker = new google.maps.Marker({
		position: position,
	    map: map
	});
	marker.setTitle("{{ point }}");
	addListerner(marker, infowindow);

	{% endfor %}
}

function addListerner(marker, infowindow) {
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.setContent(marker.title);
		infowindow.open(marker.get('map'), marker);
	});
}

window.onload = loadScript;
