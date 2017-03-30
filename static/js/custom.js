/*
	Scripts for Sympathique - V1.0
*/

$(window).load(function() {
	
	// PORTFOLIO SLIDES //
	$('#slides').slides({
		preload: true,
		preloadImage: 'images/nivo-preloader.gif',
		play: 0,
		pause: 0,
		effect: 'fade',
		autoHeight: true,
		effects: {
		 navigation: 'fade',  // [String] Can be either "slide" or "fade"
		 pagination: 'fade' // [String] Can be either "slide" or "fade"
		},
		hoverPause: true
	});
});


	// HOMEPAGE SLIDER //
	var api;
	var api2;
	
jQuery(document).ready(function() {
	api =  jQuery('.fullwidthbanner').revolution(
		{
			delay:9000,
			startheight:450,
			startwidth:1120,

			hideThumbs:200,

			thumbWidth:100,							// Thumb With and Height and Amount (only if navigation Tyope set to thumb !)
			thumbHeight:50,
			thumbAmount:5,

			navigationType:"bullet",					//bullet, thumb, none, both		(No Thumbs In FullWidth Version !)
			navigationArrows:"verticalcentered",		//nexttobullets, verticalcentered, none
			navigationStyle:"round",				//round,square,navbar

			touchenabled:"on",						// Enable Swipe Function : on/off
			onHoverStop:"on",						// Stop Banner Timet at Hover on Slide on/off

			navOffsetHorizontal:0,
			navOffsetVertical:0,

			stopAtSlide:-1,
			stopAfterLoops:-1,

			shadow:0,								//0 = no Shadow, 1,2,3 = 3 Different Art of Shadows  (No Shadow in Fullwidth Version !)
			fullWidth:"on"							// Turns On or Off the Fullwidth Image Centering in FullWidth Modus
		});
		
	api2 =  jQuery('.banner').revolution(
		{
			delay:9000,
			startheight:450,
			startwidth:1120,

			hideThumbs:200,

			thumbWidth:100,							// Thumb With and Height and Amount (only if navigation Tyope set to thumb !)
			thumbHeight:50,
			thumbAmount:5,

			navigationType:"bullet",					//bullet, thumb, none, both		(No Thumbs In FullWidth Version !)
			navigationArrows:"verticalcentered",		//nexttobullets, verticalcentered, none
			navigationStyle:"round",				//round,square,navbar

			touchenabled:"on",						// Enable Swipe Function : on/off
			onHoverStop:"on",						// Stop Banner Timet at Hover on Slide on/off

			navOffsetHorizontal:0,
			navOffsetVertical:0,

			stopAtSlide:-1,
			stopAfterLoops:-1,

			shadow:0,								//0 = no Shadow, 1,2,3 = 3 Different Art of Shadows  (No Shadow in Fullwidth Version !)
			fullWidth:"on"							// Turns On or Off the Fullwidth Image Centering in FullWidth Modus
		});		
		
	


	
  
});

// ABOUT US SKILLS
var Skills = new
function() {

    var wrapper = document.getElementById('skills');

    var $skills = {
        photoshop: '90%',
        wordpress: '80%',
        jquery: '100%',
        illustrator: '40%',
        ajax: '55%'
    };


    var create = function() {

        var html = '';
        for (var i in $skills) {

            var skill = i;
            var value = $skills[i];

            html += '<div class="row">';
            html += '<div class="skill"><p data-width="' + value + '"></p></div>';
            html += '<h2>' + skill + '</h2>';			
            html += '</div>';

        }


        $(wrapper).html(html);

    };

    var animation = function() {
        var delay = 0;
        $('p[data-width]', wrapper).each(function() {

            var $p = $(this);
            $p.queue('width', function(next) {

                $p.delay(delay).animate({
                    width: $p.data('width')
                }, 600, 'easeInOutExpo', next);

            });

            $p.dequeue('width');
            delay += 300;
        });

    };

    this.init = function() {
        create();

        setTimeout(function() {
            animation();
        }, 500);

    };

}();

Skills.init();