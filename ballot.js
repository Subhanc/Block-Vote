$(document).ready(function(){
    $('.ballot-button').click(function() {
        //alert(1);
        $.ajax({
            type: "POST",
            url: "https://reqres.in/api/register",
            data: {
                email: "sydney@fife",
                password: "pistol"
            },
            success: function(response) {
                console.log(response);
                //$('.passphrase').html(data);
            }
        });
    });
});