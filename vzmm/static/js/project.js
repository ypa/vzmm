/* Project specific Javascript goes here. */

//rotating among thumbs and main image
$(document).ready(function() {
	$('#thumbs img').click(function(){
		var main_src = $('#main img').attr('src');
		$('#main img').attr('src',$(this).attr('src'));
		$(this).attr('src', main_src);
	});

	$.getJSON('http://localhost:8080/api/hotels', {
	  key: 'value',
	  otherKey: 'otherValue'
	}, function(data){
	     // Handles the callback when the data returns
	     alert(data);
	});

});