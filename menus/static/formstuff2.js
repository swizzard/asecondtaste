(function() {'use strict';
	$('document').ready(function() {
		var formIndex = 1;
		var elseIndex = 0;
		var maxForms = Math.floor($(".control-group").length/3);
		var maxbooleans = maxForms - 2;
		var getFormNumber = function (elem, param) {
			var re = /\d+/;
			param = typeof param !== undefined ? param : 'id';
			return parseInt(re.exec(elem.attr(param)), 10);
			};
		var addClasses = function() {
			var controls = $(".control-group");
			var i;
			for (i = 0; i <= controls.length; i++) {
				var controlIDNumber = Math.floor(i/3);
				var newClass = controls.eq(i).children("label").text().toLowerCase() + " " + controlIDNumber;
				controls.eq(i).addClass(newClass);
				}
			};
		var setPlaceHolder = function() {
			var text = $(this).parents('label').text().replace(/^\s*/,''); //lstrip adapted from http://turbo-technical-report.blogspot.com/2006/11/trim-ltrim-rtrim-strip-lstrip-rstrip.html
			var num = getFormNumber($(this),'name');
			var q = $("#id_form-"+num+"-query");
			q.attr("placeholder",text);
			};
		var toCourseSelect = function() {
			var formNumber = getFormNumber($(this),'name');
			var inputToChange = $("#id_form-"+formNumber+"-query");
			var id = inputToChange.attr('id');
			var name = inputToChange.attr('name');
			var courseSelect = ['<select name="',name,'" id="',id,'">',
								'<option value="" disabled=True>Course</option>',
                                '<option value="Appetizer">Appetizer</option>',
                                '<option value="Main">Main Course</option>',
                                '<option value="Dessert">Dessert</option>',
                                '<option value="Unclassified">Unclassified</option>',
                                '</select>'].join('');
			inputToChange.parents(".controls").html(courseSelect);
			};
		var getPeriodArray = function () {
			var y;
			var periodArray = [];
			for (y=1800; y<=1995; y+=5) {
              var period;
				period = [y, "-", y+5].join('');
				periodArray.push(period);
				}
			return periodArray;
			};
		var periodArray = getPeriodArray();
		var toPeriodSelect = function() {
			var formNumber = getFormNumber($(this),'name');
			var inputToChange = $("#id_form-"+formNumber+"-query");
			var id = inputToChange.attr('id');
			var name = inputToChange.attr('name');
			var selectArray = ['<select name="',name,'" id="',id,'">',
								'<option value="" disabled=True>Period</option>',
								'</select>'];
			var i;
			for (i = 0; i <= periodArray.length; i++) {
				var offset = i + 6;
				var opt = ['<option value="',periodArray[i],'">',periodArray[i],'</option>'].join('');
				selectArray.splice(offset, 0, opt);
				}
			var periodSelect = selectArray.join('');
			inputToChange.parents('.controls').html(periodSelect);
				};
		var toTextInput = function() {
			var formNumber = getFormNumber($(this),'name');
			var inputToChange = $("#id_form-"+formNumber+"-query");
			var id = inputToChange.attr('id');
			var name = inputToChange.attr('name');
			var textInput = ['<input id="',id,'" maxlength="255" name="',name,'" type="text"/>'].join('');
			inputToChange.parents('.controls').html(textInput);
			};
		var autoClick = function(index) {
			$(".parameter."+index+" input").eq(index).click();
			setPlaceHolder();
			};
		var hideBools = function() {
			$(".boolean").hide();
			};
		var hideExtraForms = function() {
			var i;
			for (i = formIndex; i <= maxForms; i++) {
				$(".control-group."+i).hide();
				}
			};
		var showBools = function() {
			var bool = $("div.boolean."+elseIndex);
			if (elseIndex < maxbooleans) {
				bool.show();
				bool.find("input").show();
				}
			};
		var showNextForm = function() {
			$(".control-group."+formIndex).show();
			$(".boolean."+formIndex).hide();
			};
		var onMore = function() {
			showBools();
			showNextForm();
			autoClick(formIndex);
			formIndex++;
			elseIndex++;
			};
		$(".query.0 input").attr("placeholder","Dish Name");
		addClasses();
		hideExtraForms();
		hideBools();
		$("input.parameter[value!=course][value!=period]").on('click', toTextInput);
		$("input.parameter[value!=course][value!=period]").on('click',setPlaceHolder);
		$("input.parameter[value=course]").on('click',toCourseSelect);
		$("input.parameter[value=period]").on('click',toPeriodSelect);
		autoClick(elseIndex);
		$("#more").on('click',onMore);
		$(".query").filter(":gt(0)").css("border-top","1px solid black");
		});
            })();
