$(document).ready(function(){
    $('form').submit(function(event) {
        var passphrase = $('input[name=passphrase1]').val() + $('input[name=passphrase2]').val() + $('input[name=passphrase3]').val() + $('input[name=passphrase4]').val() + $('input[name=passphrase5]').val() + $('input[name=passphrase6]').val()
        var ballotData = {
            'passphrase' : passphrase,
            'vote': {
                'POTUS': $('input[name=exampleRadios]:checked').val()
            }
        }
        console.log(ballotData);
        $.ajax({
            type: "POST",
            url: "https://reqres.in/api/register",
            data: ballotData,
            success: function(response) {
                console.log(response);
            }
        });
        event.preventDefault();
    })
    /*
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
    }); */
});