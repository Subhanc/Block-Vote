$(document).ready(function(){
    $('.generate-passphrase').click(function() {
        alert(1);
        $.ajax({
            type: "GET",
            url: "https://reqres.in/api/users?page=2",
            success: function(data) {
                console.log(data);
                //$('.passphrase').html(data);
            }
        });
    });
});

