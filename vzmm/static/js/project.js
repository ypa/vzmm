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


    // initialize the validator
    $('#review_form').validate({
	  	ignore: [],
	  	//errorClass: "label-important",
        highlight: function(element, errorClass, validClass) {
            $(element).parents("div[class='review_form']").addClass("error");

        },
        unhighlight: function(element, errorClass, validClass) {
            $(element).parents(".error").removeClass("error");
        },
        errorElement: 'span',
        errorPlacement: function($error, $element) {
            $error.addClass("label label-important").insertAfter($element);
        }
	});

	$('#write_review').click(function(){
		$("#reviews").removeClass('active');
		$("#myTab li:nth-child(1)").removeClass('active');
		$("#myTab li:nth-child(2)").addClass('active');
		$("#submit").addClass('active');
		$("html, body").animate({ scrollTop: $(document).height() }, "slow");
		return false;
	});


	$('#map_canvas').gmap().bind('init', function(ev, map) {
		var lat = $('#map_canvas').attr('lat');
		var lng = $('#map_canvas').attr('long');
		var pos = lat + ',' + lng;
		var content = $('#map_canvas').attr('content');
		$('#map_canvas').gmap('addMarker', {'position': pos, 'bounds': true}).click(function() {
			$('#map_canvas').gmap('openInfoWindow', {'content': content}, this);
		});
		$('#map_canvas').gmap('option', 'zoom', 15);
	});



});