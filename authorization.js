$('.generate-passphrase').click(function() {
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/",
        success: function(data) {
            console.log(data);
            $('.passphrase').html(data);
        }
    });
});