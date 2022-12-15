'use strict';
console.log('inicio');
//funcion que escribe un texto en la consola tras dos segundos

function escribeTras2Segundos(texto,callback){
    setTimeout(() => {
        console.log(texto);
        callback();
    },2000)
}

escribeTras2Segundos('texto1', () => {
    escribeTras2Segundos('texto2',() => {
        console.log('fin');
    })
    
});

