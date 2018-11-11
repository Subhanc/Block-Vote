$(document).ready(function(){
    $('.ballot-button').click(function() {
        alert(1);
        $.ajax({
            type: "POST",
            url: "https://reqres.in/api/users",
            data: {
                name: "Donald J. Trump",
                job: "POTUS"
            },
            success: function(response) {
                console.log(response);
                //$('.passphrase').html(data);
            }
        });
    });
});