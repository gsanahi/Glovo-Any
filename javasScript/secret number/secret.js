import readline from 'readline';

// Configuración de mínimo y máximo.
// Cálculo del número secreto.

function calculateRandonNum (min,max) {
    const randomNum = Math.floor(Math.random() * (max-min + 1)) + min;
    return randomNum;
}

const secretNumber = calculateRandonNum(0,100);

//Pedir número al usuario.

console.log(secretNumber);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function getNumberfromConsole(){
    const promise = new promise((resolve, reject) => {       
        rl.question('introduce el numero:', (num) => {
            rl.pause();
            resolve(num)
        })
    })
    return promise;
}

const numberFromConsole = await getNumberfromConsole()

console.log(numberFromConsole)

//Comprobar si el número es el número secreto:
//Si lo es, tenemos ganador!
//Si no lo es, damos la pista