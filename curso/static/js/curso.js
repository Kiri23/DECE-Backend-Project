console.log("Hey working in curso")

$(".read-more").click(function () {
    if ($(this).hasClass("more")) {
        console.log("Tiene clase more")
        $(this).html("{{curso.descripcion| truncatewords:28}}")
        $(this).removeClass("more")
    } else {
        console.log("No tiene clases more show full text")
        console.log($(this).prev())
        console.log(descriptionText)
        $(".description-text").html("{{curso.descripcion}}")
        $(this).addClass("more")
    }
})