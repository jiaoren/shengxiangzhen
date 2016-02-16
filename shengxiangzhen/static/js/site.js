$(document).ready(function(){
	$('.thumbnails li[category!=jelly]').hide();
	
	$("a.jelly").click(function(){
		$('.thumbnails li[category!=jelly]').hide();
		$('.thumbnails li[category=jelly]').show();
	});
	
	$("a.beans").click(function(){
		$('.thumbnails li[category!=beans]').hide();
		$('.thumbnails li[category=beans]').show();
	});
	
	
	$("a.cookie").click(function(){
		$('.thumbnails li[category!=cookie]').hide();
		$('.thumbnails li[category=cookie]').show();
	});
	
	
	$("a.snack").click(function(){
		$('.thumbnails li[category!=snack]').hide();
		$('.thumbnails li[category=snack]').show();
	});
	
	$("a.giftset").click(function(){
		$('.thumbnails li[category!=giftset]').hide();
		$('.thumbnails li[category=giftset]').show();
	});
});
