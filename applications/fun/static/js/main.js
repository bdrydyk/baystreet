$(document).ready(function(){
	$('form').ajaxForm(function() { 
		alert("Thank you for your comment!"); 
		}); 
  	$("p").dblclick(function(){
    	$(this).css("color","red")
    		.hide(1000)
    		.show(2000)
    		.css("color","green")
    		.hide(1000);
  	});
$('.hand-container').magnificPopup({
  delegate: 'a', // child items selector, by clicking on it popup will open
  type: 'image'
  // other options
});




});
