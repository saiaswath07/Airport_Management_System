
	$(".nav li").on("click", function() {
      $(".nav li").removeClass("active");
      $(this).addClass("active");
    });
    function navbar_movment(event)
	{
        	$(event.data.param1).slideToggle("fast");

	};

  
