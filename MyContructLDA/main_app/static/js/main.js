$('#search-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : '/search/',
        method : 'GET',
        data : { search : $('#search-text').val() },
        
        success : function(json){
            var element = $('#result-list');
            element.empty()
            for ( var i = 0, l = json.results.length; i < l; i++ ) {
                element.append('<li class="list-group-item">' +
                               '<a href="' + json.results[i].link + '">'  + 
                               json.results[i].name + '</a></li>');
            }
        }
    });
});


// Função para o menu ficar com a class = active
$(function(){
		$('#cssmenu a').filter(function(){return this.href==location.href}).parent().addClass('active').siblings().removeClass('active')
		$('#cssmenu a').click(function(){
			$(this).parent().addClass('active').siblings().removeClass('active')	
		})
	})

////////////////////////////////////////////////


$('button').on('click', function(event){
    event.preventDefault();
    var element = $(this);

    $.ajax({
        url : '/like_treasure/',
        type : 'POST',
        data : { projeto_id : $(this).attr("data-id")},

        success : function(data){
            element.html(' ' + data);
        }
    });
});


// You need these methods to add the CSRF token using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
