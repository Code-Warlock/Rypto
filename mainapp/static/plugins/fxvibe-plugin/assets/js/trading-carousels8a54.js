(function($) {
	
	"use strict";
	var trading_carousels_script_js = function($scope, $) {
		
		// four-item-carousel
		if ($('.four-item-carousel').length) {
			var slider_attr = $('.four-item-carousel').data('trading-slider');
			$('.four-item-carousel').owlCarousel({
				loop:slider_attr.loop,
				margin:slider_attr.spacebetween,
				nav:true,
				smartSpeed: 500,
				autoplay: 1000,
				navText: [ '<span class="flaticon-left"></span>', '<span class="flaticon-right-arrow-1"></span>' ],
				responsive:{
					0:{
						items:1
					},
					480:{
						items:1
					},
					600:{
						items:2
					},
					800:{
						items:3
					},			
					1200:{
						items:slider_attr.slidesperview
					}
				}
			});    		
		}
		
		
		// three-item-carousel
		if ($('.three-item-carousel').length) {
			var slider_attr_two = $('.three-item-carousel').data('trading-slider-two');
			$('.three-item-carousel').owlCarousel({
				loop:slider_attr_two.loop,
				margin:slider_attr_two.spacebetween,
				nav:true,
				smartSpeed: 500,
				autoplay: 1000,
				navText: [ '<span class="flaticon-left"></span>', '<span class="flaticon-right-arrow-1"></span>' ],
				responsive:{
					0:{
						items:1
					},
					480:{
						items:1
					},
					600:{
						items:2
					},
					800:{
						items:2
					},			
					1200:{
						items:slider_attr_two.slidesperview
					}
				}
			});    		
		}
		
	};
	$(window).on('elementor/frontend/init', function () {
		elementorFrontend.hooks.addAction('frontend/element_ready/fxvibe_trading_carousel.default', trading_carousels_script_js);
    });	

})(window.jQuery);