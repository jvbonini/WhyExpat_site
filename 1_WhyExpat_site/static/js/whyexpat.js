(function($){
	var alreadyFixed = false;
	function init()
	{
		$('video').hover(function toggleControls() {
		    if (this.hasAttribute("controls")) {
		        this.removeAttribute("controls")
		    } else {
		        this.setAttribute("controls", "controls")
		    }
		});

		onScroll();
		$(window).scroll(onScroll);

		$(".boton-volver").bind("click", function(e){
			e.preventDefault();
				$("body,html").animate({"scrollTop":0}, 400);
			return false;
		});

	}

	function onScroll()
	{
		
		if ($(window).scrollTop() >= 92 && alreadyFixed == false)
		{
			$("aside").addClass("fixed");
			alreadyFixed = true;
		}else if ($(window).scrollTop() < 92 ){
			$("aside").removeClass("fixed");
			alreadyFixed = false;
		}
	}

	$("document").ready(init);
})(jQuery);