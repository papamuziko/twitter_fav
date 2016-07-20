
$("#search").keypress(function(e) {
    if(e.which == 13) {
        $.post("/search", { q: $(this).val() }, function(result) {

        });
    }
});