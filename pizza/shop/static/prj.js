

    function success(data){

        if(data.status==0){
            $('#login_form').hide();
            $('#logout_link').show();
        }
        alert(data.message);
    }

    function ajax_login(){

    data = {
        'login': $('#login_field').val(),
        'password':  $('#pwd_field').val(),
        'csrfmiddlewaretoken': $( "[name='csrfmiddlewaretoken']" ).val()
    }

    $.ajax({
        type: "POST",
        url: "/account/alogin",
        data: data,
        success: success
    });

    }

    $('#login_link').on('click',ajax_login);
