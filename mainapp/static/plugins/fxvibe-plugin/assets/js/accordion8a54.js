(function($) {
	
	"use strict";
	var accordion_script_js = function($scope, $) {
		
		//Accordion Box
		function accordionActive() {
			if($('.accordion-box').length){
				$(".accordion-box").on('click', '.acc-btn', function() {
					
					var outerBox = $(this).parents('.accordion-box');
					var target = $(this).parents('.accordion');
					
					if($(this).hasClass('active')!==true){
						$(outerBox).find('.accordion .acc-btn').removeClass('active');
					}
					
					if ($(this).next('.acc-content').is(':visible')){
						return false;
					}else{
						$(this).addClass('active');
						$(outerBox).children('.accordion').removeClass('active-block');
						$(outerBox).find('.accordion').children('.acc-content').slideUp(300);
						target.addClass('active-block');
						$(this).next('.acc-content').slideDown(300);	
					}
				});	
			}
		}
		accordionActive();
		
	};
	$(window).on('elementor/frontend/init', function () {
            elementorFrontend.hooks.addAction('frontend/element_ready/fxvibe_faqs.default', accordion_script_js);
			elementorFrontend.hooks.addAction('frontend/element_ready/fxvibe_faq_tabs.default', accordion_script_js);
    });	

})(window.jQuery);