DEBUG = false
// Shorthand for document.ready()
$(function () {
    var categoriasChecked = []
    // for each checkbox listen for a change event and update the list of course displaying
    $(".categoriaCheckbox").each(function () {
        $(this).change(function () {
            checkBox = this
            // testThis(checkBox)
            updateCursoList(checkBox, categoriasChecked)
        });
    });
})

/**
 * Esta funcion actualiza la lista de curso en la pagina de inicio
 */
function updateCursoList(checkBox, checkBoxArr) {
    if (checkBox.checked) {
        checkBoxArr.push(checkBox.value)
    } else if (!checkBox.checked) {
        removeCategory(checkBoxArr, checkBox)
    }
    updateCursoAjax(checkBoxArr)
}
/**
 * Remueve la categoria especificada de la lista de checkbox
 */
function removeCategory(checkBoxArr, checkBox) {
    var index = checkBoxArr.indexOf(checkBox.value);
    if (index > -1) {
        checkBoxArr.splice(index, 1);
        if (checkBoxArr.length == 0) {
            // No categories checkbox is selected.Send Todos to list all course
            return updateCursoAjax('Todos')
        }
    }
}

/**
 * La llamada ajax que utilizó para actualizar los cursos al momento cuando se elige una categoria 
 * @param {List} categorias - Por las categorias que voy a filtrar los cursos
 */
function updateCursoAjax(categorias) {
    var data = { 'categoria': categorias }
    debugLog(data, DEBUG)
    // Ajax Call. The URL is pass in the inicio.html template
    $.get(URL, data).done(function (listaDeCurso) {
        console.log("fue succesful la llamada de Ajax")
        var html = createHtml(listaDeCurso.cursos)
        $('.curso').html(html)
    })
        .fail(function (s, d, e) {
            console.log("Hubo un error en la llamada ajax", e)
        });
}

function createHtml(listaDeCurso) {
    var html = `
        <section class="curso">
    <div class="container">
        <div class="row">
    `
    for (index = 0; index < listaDeCurso.length; index++) {
        html += `<div class="col-sm-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title titulo_curso">` + listaDeCurso[index].titulo + `</h5>
                        <p class="card-text">`+ listaDeCurso[index].descripcion + `
                        </p>
                        <a href="curso/`+ listaDeCurso[index].id + ` " class="btn btn-primary">Ver mas</a>
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



// Helper Methods
function debugLog(data, isDebug) {
    if (DEBUG) {
        console.log(data, 'Las categorias que se van a enviar a llamada Ajax')
    }
}
