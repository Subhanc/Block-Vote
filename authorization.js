$('.generate-passphrase').click(function() {
    $.ajax({
        type: "GET",
        url: "https://jsonplaceholder.typicode.com/todos/1",
        success: function(data) {
            console.log(data);
            $('.passphrase').html(data);
        }
    });
});