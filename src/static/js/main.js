(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });

})(jQuery);



// var placeholder = "Type your text here..."; //Change this to your placeholder text
// $("#Text_box").focus(function() {
// 	if ($(this).text() == placeholder) {
// 		$(this).text("");
// 	}
// }).focusout(function() {
// 	if (!$(this).text().length) {
// 		$(this).text(placeholder);
// 	}
// });
