$(document).ready(init);

function init() {
	var map;
	var mapOption = { 
		div: '#map', 
		zoom: 12,
		lat: 23.37, 
		lng: 116.71 
	};
	map = new GMaps(mapOption);
}
