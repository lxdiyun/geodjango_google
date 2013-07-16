function initialize() {
	var mapOptions = {
		zoom: 13,
		center: new google.maps.LatLng(23.37, 116.71),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	var map = new google.maps.Map(document.getElementById('map-canvas'),
				      mapOptions);
}

function loadScript() {
	var script = document.createElement('script');
	script.type = 'text/javascript';
	script.src = 'http://ditu.google.cn/maps/api/js?key={{ GOOGLE_MAPS_API_KEY }}&language=zh-CN&sensor=false&' +
		'callback=initialize';
	document.body.appendChild(script);
}

window.onload = loadScript;
