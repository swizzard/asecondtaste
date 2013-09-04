//form stuff
	$('document').ready(function() {
		//reusable function to number form elements
		var numberFormElements = function() {
			var formElements = $("form").children();
			var i;
			var newID;
			for (i = 0; i <= formElements.length; i++) {
				var thisElement = formElements.eq(i);
				if (thisElement.attr('id') !== undefined) {
					newID = thisElement.attr('id') + i;
					thisElement.attr('id', newID);
					}
				else if (thisElement.attr('class') === 'parameter') {
					newID = 'parameter' + i;
					thisElement.attr('id', newID);
					}
				}
			};

		//reusable function to retrieve form element numbers
		var getElementIDNumber = function(formElement) {
			var re = /\d+/;
			return parseInt(re.exec(formElement.attr('id')), 10);
			};

		//reusable function to change placeholder text
		var setPlaceholder = function(input) {
			var checked = input.children().filter("[checked=checked]");
			input.attr("placeholder", checked.text());
			};

		//reusable function to autocheck radios
		var checkI = function(searchFormDiv) {
			var i = getElementIDNumber(searchFormDiv);
			searchFormDiv.children(".parameter").eq(i).attr("checked","checked");
			setPlaceholder(searchFormDiv);
			};

		//show bool options, add another form (while hiding the new form's bool options), and renumber everything
		var onMore = function() {
			$('this').next().show();
			$("#submit").before($(".search-form0").html());
			var newForm = $(".search-form").last();
			newForm.children().filter("[id^=bool]").hide();
			numberFormElements();
			checkI(newForm);
			};


		//stuff that happens on document.ready/in general
		numberFormElements();
		$("input").filter("[type=radio]").on('click', setPlaceholder($('this').parent()));
		$("label").filter("[id^=bool]").hide(); //hide first bool radios
		$(".more").on('click',onMore());

	});
