
const button1 = document.querySelector('#button-imperative');

// añadimos evento click al botón 1 e indicamos la función que queremos que se ejecute cuando el evento suceda.
button1.addEventListener("click", buttonClicked)

// esta linea es exactamente igual a la anterior
// button1.addEventListener("click", () => { console.log('se ha pulsado el botón'); })

// añadimos evento mouseover.
button1.addEventListener("mouseover", (event) => {
  console.log(event);
})

function buttonClicked() {
  console.log('se ha pulsado el botón');
}