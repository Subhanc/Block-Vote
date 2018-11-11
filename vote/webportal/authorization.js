$(document).ready(function(){
    $('.generate-passphrase').click(function() {
        $.ajax({
            type: "GET",
            url: "http://localhost:5000/",
            success: function(data) {
                 console.log(data);
                 $('p').text(data);
                $('.passphrase').html(data);
            }
        });
    });
});

