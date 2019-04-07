// Shorthand for document.ready()
$(function () {
    var categoriasChecked = []
    $(".categoriaCheckbox").each(function () {
        console.log($(this).prop('checked'))
        $(this).change(function () {
            if (this.checked){
                categoriasChecked.push(this.value)
            }else if (!this.checked){
                // remove specify item by value
                var index = categoriasChecked.indexOf(this.value);
                if (index > -1) {
                    console.log('se va a remover')
                    categoriasChecked.splice(index, 1);
                    if (categoriasChecked.length == 0){
                        console.log('el array no tiene ningun elemento')
                        return updateCurso('Todos')
                    }
                }
            }
            console.log('array', categoriasChecked)
            console.log(this.checked)
            updateCurso(categoriasChecked)
        });
    });
})

function updateCurso(categorias){
    console.log(categorias[0], 'array in update curso')
    var data = {'categoria': categorias}
    console.log(data, 'array in update curso')
    $.get(URL, data).done(function(listaDeCurso){
        console.log("fue succesful la llamada de Ajax")
        // console.log(listaDeCurso.cursos)
        var html = createHtml(listaDeCurso.cursos)
        // console.log(listaDeCurso.cursos[0].titulo)
        // console.log(html)
        $('.curso').html(html)
        // window.location.search += 'categoria='+categorias;
    })
    .fail(function(s,d,e){
        console.log("Hubo un error en la llamada ajax", e)
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
