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

	$.fn.stars = function() {
	    return $(this).each(function() {
	        // Get the value
	        var val = parseFloat($(this).html());
	        // Make sure that the value is in 0 - 5 range, multiply to get width
	        var size = Math.max(0, (Math.min(5, val))) * 16;
	        // Create stars holder
	        var $span = $('<span />').width(size);
	        // Replace the numerical value with stars
	        $(this).html($span);
	    });
	}

	$(function() {
    	$('span.stars').stars();
	});

	$(function () {
		$('#myTab a:first').tab('show');
		$('#myTab a').click(function (e) {
			e.preventDefault();
			$(this).tab('show');
		});
	});


	$.validator.addMethod('minStrict', function (value, el, param) {
	    return value > param;
	});

    //2. Include custom validation in the rules for your element
    $("#review_form").validate(
    {
		score: {
		    required: true,
		    minStrict: 0,
		    number: true
		}
    });

	$("#review_form").validate();

	$(function() {
		$errorDiv = $('<div>hello</div>').addClass('error');
		if ($("#rateit").rateit('value') <= 0) {
			$("#rateit").append($errorDiv);
		}
	});


});