// Configuración de mínimo y máximo.

funtion calculateRandonNum (min,max) {
    const randomNum = Math.floor(Math.random() * (max-min + 1)) + min;
    return randomNum;
}




Cálculo del número secreto.
Pedir número al usuario.
Comprobar si el número es el número secreto:
Si lo es, tenemos ganador!
Si no lo es, damos la pista