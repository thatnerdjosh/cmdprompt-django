(function($) {

	skel
		.breakpoints({
			desktop: '(min-width: 737px)',
			tablet: '(min-width: 737px) and (max-width: 1200px)',
			mobile: '(max-width: 736px)'
		})
		.viewport({
			breakpoints: {
				tablet: {
					width: 1080
				}
			}
		});

	$(function() {

		var	$window = $(window),
			$body = $('body');

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				$body.removeClass('is-loading');
			});

		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on mobile.
			skel.on('+mobile -mobile', function() {
				$.prioritize(
					'.important\\28 mobile\\29',
					skel.breakpoint('mobile').active
				);
			});

		// CSS polyfills (IE<9).
			if (skel.vars.IEVersion < 9)
				$(':last-child').addClass('last-child');

		// Dropdowns.
			$('#nav > ul').dropotron({
				mode: 'fade',
				noOpenerFade: true,
				speed: 300,
				alignment: 'center'
			});

		// Off-Canvas Navigation.

			// Title Bar.
				$(
					'<div id="titleBar">' +
						'<a href="#navPanel" class="toggle"></a>' +
						'<span class="title">' + $('#logo').html() + '</span>' +
					'</div>'
				)
					.appendTo($body);

			// Navigation Panel.
				$(
					'<div id="navPanel">' +
						'<nav>' +
							$('#nav').navList() +
						'</nav>' +
					'</div>'
				)
					.appendTo($body)
					.panel({
						delay: 500,
						hideOnClick: true,
						hideOnSwipe: true,
						resetScroll: true,
						resetForms: true,
						side: 'left',
						target: $body,
						visibleClass: 'navPanel-visible'
					});

			// Fix: Remove navPanel transitions on WP<10 (poor/buggy performance).
				if (skel.vars.os == 'wp' && skel.vars.osVersion < 10)
					$('#titleBar, #navPanel, #page-wrapper')
						.css('transition', 'none');

	});

})(jQuery);

(function($){
	function equalizeHeights(selector, selectorChange) {

		// Loop to get all element heights
		$(selector).each(function() {
				var heights = new Array();
			    childElements = $(this).find('.profile')
			    childElements.each(function() {
					// Need to let sizes be whatever they want so no overflow on resize
					$(this).css('min-height', '0');
					$(this).css('max-height', 'none');
					$(this).css('height', 'auto');

					// Then add size (no units) to array
					heights.push($(this).height());
				});
				// Find max height of all elements
				var max = Math.max.apply( Math, heights ) + 20;

				// Set all heights to max height
				childElements.each(function() {
					$(this).css('height', max + 'px');
				});			
		});
	
	}
	if($('div.row:has(section.profile)').length) {

	    $(window).load(function() {
		// Fix heights on page load
		equalizeHeights(".box.features .row", "section.profile");

		// Fix heights on window resize
		$(window).resize(function() {

			// Needs to be a timeout function so it doesn't fire every ms of resize - rename MYSELECTOR
      // class type that needs resizing
			setTimeout(function() {
	      		equalizeHeights(".box.features .row", "section.profile");
			}, 120);
		});
	    });
	}
})(jQuery);


