(function($) {
	
	"use strict";
	var client_carousels_script_js = function($scope, $) {
		
		//bx slider
		if ($('.featured-section .featured-slider').length) {
			var slider_attr = $('.featured-section .featured-slider').data('client-slider');
			$('.featured-section .featured-slider').bxSlider({
				nextText: '<i class=""></i>',
				prevText: '<i class=""></i>',
				auto: slider_attr.loop,
				speed: '700',
				mode:'vertical',
				maxSlides: slider_attr.slidesperview,
				minSlides: slider_attr.slidesperview,
				moveSlides: 1,
				pagerCustom: '.testimonial-style-two .slider-pager .thumb-box'
			});
		}
		
		
		// five-item-carousel
		if ($('.five-item-carousel').length) {
			var slider_attr_two = $('.five-item-carousel').data('client-slider-two');
			$('.five-item-carousel').owlCarousel({
				loop:slider_attr_two.loop,
				margin:slider_attr_two.spacebetween,
				nav:true,
				smartSpeed: 500,
				autoplay: 1000,
				navText: [ '<span class="flaticon-thin-right-straight-arrow"></span>', '<span class="flaticon-thin-right-straight-arrow"></span>' ],
				responsive:{
					0:{
						items:1
					},
					480:{
						items:2
					},
					600:{
						items:3
					},
					800:{
						items:4
					},			
					1200:{
						items:slider_attr_two.slidesperview
					}
	
				}
			});    		
		}	
		
	};
	$(window).on('elementor/frontend/init', function () {
		elementorFrontend.hooks.addAction('frontend/element_ready/fxvibe_client_carousel.default', client_carousels_script_js);
    });	

})(window.jQuery);