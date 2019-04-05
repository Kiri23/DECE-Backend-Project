console.log("Hola from Inicio.js")
console.log($)
var waitForJQuery = setInterval(function () {
    if (typeof $ != 'undefined') {

        // place your code here.
        console.log('waiting')
        clearInterval(waitForJQuery);
    }
}, 10);