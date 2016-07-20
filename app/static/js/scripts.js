
$("#search").keypress(function(e) {
    if(e.which == 13) {
        $.post("/search", { q: $(this).val() }, function(result) {
            console.log(result);
            var json = jQuery.parseJSON(result);
            var container = $("<div />");
            for(var i=0, l = json.length ; i < l ; i ++) {
                var item = json[i];
                container.append('<a href="'+item.url+'" target="_blank">'+item.text+'</a><br/>');
            }
            $("#result").html(container);
        });
    }
});