$(document).ready(function(){
    $('form').submit(function(event) {
        var passphrase = $('input[name=passphrase1]').val() + $('input[name=passphrase2]').val() + $('input[name=passphrase3]').val() + $('input[name=passphrase4]').val() + $('input[name=passphrase5]').val() + $('input[name=passphrase6]').val()
        var ballotData = {
            'passphrase' : passphrase,
            'vote': $('input[name=exampleRadios]:checked').val()
        }
        console.log(ballotData);
        $.ajax({
            type: "POST",
            url: "http://localhost:5000",
            data: ballotData,
            success: function(response) {
                console.log(response);
            }
        });
        event.preventDefault();
    })
});