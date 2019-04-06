console.log("Hola from Inicio.js")
console.log($)
// Shorthand for document.ready()
$(function () {
    console.log('hola')
    console.log(URL)
})

$(".categoriaCheckbox").each(function () {
    console.log($(this).prop('checked'))
    $(this).change(function () {
        console.log('this change', this)
        updateCurso(this.value)

    });
});

function updateCurso(categorias){
    var data = {'categoria': categorias}
    console.log('update curso data: ', data)
    $.get(URL, data).done(function(listaDeCurso){
        console.log("fue succesful la llamada de Ajax")
        // console.log(listaDeCurso.cursos)
        var html = createHtml(listaDeCurso.cursos)
        console.log(listaDeCurso.cursos[0].titulo)
        console.log(html)
        $('.curso').html(html)
        // window.location.search += 'categoria='+categorias;
    })
    .fail(function(){
        console.log("Hubo un error en la llamada ajax")
    });
}

function createHtml(listaDeCurso){
    var html = `
        <section class="curso">
    <div class="container">
        <div class="row">
    `
    for (index = 0; index < listaDeCurso.length; index++){
        html += `<div class="col-sm-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title titulo_curso">` + listaDeCurso[index].titulo+ `</h5>
                        <p class="card-text">`+listaDeCurso[index].descripcion+`
                        </p>
                        <a href="{%url 'curso:curso' curso.id%}" class="btn btn-primary">Ver mas</a>
                    </div>
                </div>
            </div>`
    }
    html += `
          </div>
    </section>
    `
    return html
}
