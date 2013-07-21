
$(document).ready(init);

function init() {
	var map;
	var mapOption = { 
		div: '#map', 
		zoom: 13,
		lat: 23.37, 
		lng: 116.71 
	};
	map = new GMaps(mapOption);

	addMarker(map);
}

function addMarker(map) {
	var marker;
	var infowindow = new google.maps.InfoWindow();

	{% for point in points %}
	marker = GMaps.prototype.createMarker({
		lat: {{ point.latitude }},
		lng: {{ point.longitude }},
		title: "{{ point }}"
	});
	map.addMarker(marker);
	addListerner(marker, infowindow);

	{% endfor %}
}

function addListerner(marker, infowindow) {
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.setContent(marker.title);
		infowindow.open(marker.get('map'), marker);
	});
}
