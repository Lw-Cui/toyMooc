/**
 * Created by lw on 15-7-28.
 */
$(document).ready(function() {
    $(".choose").click(function() {
        $(this)
            .text("Chosed!")
            .css("color", "blue");
        $.post("/add_course/", {
            title: $(this).attr("name")
            }, function(data, status) {
        })
    });
    $(".cancel").click(function() {
        $(this)
            .text("Canceled")
            .css("color", "red");
        $.post("/cancel_course/", {
            title: $(this).attr("name")
            }, function(data, status) {
        })
    });
});