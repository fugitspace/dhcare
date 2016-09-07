getPercentage = function(y_cug, no_cug){
    var cug = parseInt(y_cug);
    var not_cug = parseInt(no_cug);
    var total = parseInt(y_cug)+parseInt(no_cug);
    console.log("The total is "+total);
    var in_cug = (parseInt(y_cug)/parseInt(total)).toFixed(2);
    var not_in_cug = (parseInt(no_cug)/parseInt(total)).toFixed(2);  
    return {"in_cug":in_cug, "not_in_cug":not_in_cug};
    
}


searchByDate = function(search_url, start_date, end_date, data_type){
    console.log("The date is "+start_date);
    var query;
    if(start_date.length == 0 && end_date.length > 0){
	query = { "start_date": start_date };
    }
    else if (start_date.length > 0 && end_date.length == 0){
	query = { "end_date": end_date };
    }
    else if (start_date.length > 0 && end_date.length > 0){
	query = {
	    "start_date": start_date,
	    "end_date": end_date
	}
    }


    // Using the core $.ajax() method
    $.ajax({
	
	// The URL for the request
	url: search_url,
	
	// The data to send (will be converted to a query string)
	data: query,
	// Whether this is a POST or GET request
	type: "GET",
	
	// The type of data we expect back
	dataType : data_type,
    })
    // Code to run if the request succeeds (is done);
    // The response is passed to the function
	.done(function( json ) {	    	    
	    $( "<h1>" ).text( json.name ).appendTo( "body" );
	    $( "<div class=\"content\">").html( json.html ).appendTo( "body" );
	})
    // Code to run if the request fails; the raw request and
    // status codes are passed to the function
	.fail(function( xhr, status, errorThrown ) {
	    alert( "Sorry, there was a problem!" );
	    console.log( "Error: " + errorThrown );
	    console.log( "Status: " + status );
	    console.dir( xhr );
	})
    // Code to run regardless of success or failure;
	.always(function( xhr, status ) {
	    console.log( "The request is complete!" );
	});
    
}



$('.third.circle').circleProgress({
    value: 0.75,
    fill: { gradient: [['#0681c4', .5], ['#4ac5f8', .5]], gradientAngle: Math.PI / 4 }
}).on('circle-animation-progress', function(event, progress, stepValue) {
    $(this).find('strong').text(String(stepValue.toFixed(2)).substr(1));
});

/* 
 *back to top button
*/
$(document).ready(function(){
    $(window).scroll(function () {
	if ($(this).scrollTop() > 50) {
	    $('#back-to-top').fadeIn();
	} else {
	    $('#back-to-top').fadeOut();
	}
    });
    // scroll body to 0px on click
    $('#back-to-top').click(function () {
	$('#back-to-top').tooltip('hide');
	$('body,html').animate({
	    scrollTop: 0
	}, 800);
	return false;
    });

    $('#back-to-top').tooltip('show');

});
