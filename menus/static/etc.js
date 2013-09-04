(function() {'use strict';
	$('document').ready(function() {
	var m = ['ma','il','to',':'];
	var s = ["s","ra","ke","r@","gc.", "cu","ny",".e","du"];
	var r = ["rr","ak","ov","@g","c.","cu","ny",".e","du"];
	$("#mail-sam").prop('href',function() {return m.join('')+s.join('');});
	$('#mail-rachel').prop('href',function() {return m.join('')+r.join('');});
	$("#contact-us").on('click',function() {$('#answer6').collapse('show')}); //expand contact info when 'contact us' link clicked
	//other stuff goes here, if necessary
	}
	);})();
