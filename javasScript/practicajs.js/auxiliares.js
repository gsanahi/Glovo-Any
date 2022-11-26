function calculateRandonNum (min,max) {
    const randomNum = Math.floor(Math.random() * (max-min + 1)) + min;
    return randomNum;
}

function random_item(items){
    return items[Math.floor(Math.random()*items.length)];
}

//1- Mostrar en formato de tabla todos los alumnos.

console.table(students)
//2- Mostrar por consola la cantidad de alumnos que hay en clase.

console.log(students.length)

3- Mostrar por consola todos los nombres de los alumnos.
for (let i=0; i<students.length;i++){
    console.log(students[i].name);
}

4- Eliminar el último alumno de la clase.

students.pop()

5- Eliminar un alumno aleatoriamente de la clase.
students.shift(calculateRandonNum(0,students.length))

6- Mostrar por consola todos los datos de los alumnos que son chicas.
for (let i=0; i<students.length;i++) {
    if (students.gender === 'female'){
        console.log(students[i])
    }
}


7- Mostrar por consola el número de chicos y chicas que hay en la clase.
let boys = 0
let girls = 0

for (let i=0; i<students.length;i++) {
    if (students.gender === 'female'){
        girls += 1
    } else {
        boys +=1
    }
console.log('Total boys:' + boys + 'Total girls:' + girls)
}

8- Mostrar true o false por consola si todos los alumnos de la clase son chicas.
function isGirl() {
    return students.gender === 'female'
}
console.log(students.every(isGirl(students)))

9- Mostrar por consola los nombres de los alumnos que tengan entre 20 y 25 años.
for (let i=0; i<students.length;i++){
    if (students.age >= 20 && students.age <= 25) {
        console.log(students.name)
    }
}


10- Añadir un alumno nuevo con los siguientes datos:
nombre aleatorio.
edad aleatoria entre 20 y 50 años.
género aleatorio.
listado de calificaciones vacío.
¡OJO!, el nombre y el género tienen que ir acordes.

const newStudent = {...students[0]}
newStudent.gender = random_item(availableGenders)
newStudent.name = if (newStudent.gender === 'male') {
    random_item(availableMaleNames)
} else {
    random_item(availableFemaleNames)
}

newStudent.age = calculateRandonNum(20,50)
newStudent.examScores = []


11- Mostrar por consola el nombre de la persona más joven de la clase.
¡OJO!, si varias personas de la clase comparten la edad más baja, cualquiera
de ellos es una respuesta válida.

let youngest= student.age.reduce(function(a,b){return a > b;});

const menor = students.find(students.age > 1);
console.log(menor);


12- Mostrar por consola la edad media de todos los alumnos de la clase.
let ages = []
for (let i=0; i<students.length;i++) {
    ages += students.age
}

students.age.forEach(i => ages += students.age )

console.log(ages/students.length)

13- Mostrar por consola la edad media de las chicas de la clase.
let ages = []
let amount = 0
for (let i=0; i<students.length;i++) {
    if (students.gender === 'female') {
        ages += students.age
        amount += 1
    }
}

console.log(ages/amount)


14- Añadir nueva nota a los alumnos. Por cada alumno de la clase, 
tendremos que calcular una nota de forma aleatoria(número entre 0 y 10) y 
añadirla a su listado de notas.

for (let i=0; i<students.length;i++){
     students.examScores.push(calculateRandonNum(0,10));    
}

students.examScores.forEach(element => {
    students.examScores.push(calculateRandonNum(0,10)); 
});


15- Ordenar el array de alumnos alfabéticamente según su nombre.
students.name.sort()

Requisitos opcionales
Os recomiendo encarecidamente que los intentéis, no son difíciles!

16- Mostrar por consola el alumno de la clase con las mejores notas.
El alumno con mejores notas es aquel cuyo sumatorio de todas sus notas
es el valor más alto de todos.

let best_note = student.examScores.reduce(function(a,b){return a + b;});


17- Mostrar por consola la nota media más alta de la clase y el nombre del 
alumno al que pertenece.
18- Añadir un punto extra a cada nota existente de todos los alumnos. 
Recordad que la nota máxima posible es 10. Si los alumnos 
aún no tienen registrada ninguna nota, les pondremos un 10.


