
// Função para o menu ficar com a class = active
$(function(){
		$('#cssmenu a').filter(function(){return this.href==location.href}).parent().addClass('active').siblings().removeClass('active')
		$('#cssmenu a').click(function(){
			$(this).parent().addClass('active').siblings().removeClass('active')	
		})
	})

////////////////////////////////////////////////


$('button#likes').on('click', function(event){
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


$(document).ready(function(){

        $(".wrapper").hide();

    $('.panel-project').click(function(){
    $(".wrapper").slideToggle();
    return false;
    });

});