const readline = require("readline");

const students = [
  {
    age: 32,
    examScores: [],
    gender: "male",
    name: "edu",
  },
  {
    age: 29,
    examScores: [],
    gender: "female",
    name: "silvia",
  },
];

const availableMaleNames = [
  "pepe",
  "juan",
  "victor",
  "leo",
  "francisco",
  "carlos",
];
const availableFemaleNames = [
  "cecilia",
  "ana",
  "luisa",
  "silvia",
  "isabel",
  "virginia",
];
const availableGenders = ["male", "female"];

/*
 * Funciones auxiliares
 */

// Calcula un numero random incluyendo min y max
function calculateRandomNum(min, max) {
  const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
  return randomNum;
}

function random_item(items) {
  return items[calculateRandomNum(0, items.length - 1)];
}

function isGirl(student) {
  return student.gender === "female";
}

// 1- Mostrar en formato de tabla todos los alumnos.
function ej1() {
  console.table(students);
}

// 2- Mostrar por consola la cantidad de alumnos que hay en clase.
function ej2() {
  console.log(students.length);
}

// 3- Mostrar por consola todos los nombres de los alumnos.
function ej3() {
  for (let i = 0; i < students.length; i++) {
    console.log(students[i].name);
  }
}

// 4- Eliminar el último alumno de la clase.
function ej4() {
  students.pop();
}

// 5- Eliminar un alumno aleatoriamente de la clase.
function ej5() {
  students.splice(calculateRandomNum(0, students.length - 1), 1);
}

// 6- Mostrar por consola todos los datos de los alumnos que son chicas.
function ej6() {
  students
    .filter((student) => student.gender === "female")
    .forEach((student) => console.log(student));
}

// 7- Mostrar por consola el número de chicos y chicas que hay en la clase.
function ej7() {
  let boys = 0;
  let girls = 0;

  for (let i = 0; i < students.length; i++) {
    if (isGirl(students[i])) {
      girls += 1;
    } else {
      boys += 1;
    }
  }
  console.log("Total boys:" + boys + "Total girls:" + girls);
}

// 8- Mostrar true o false por consola si todos los alumnos de la clase son chicas.
function ej8() {
  console.log(students.every(isGirl));
}

// 9- Mostrar por consola los nombres de los alumnos que tengan entre 20 y 25 años.
function ej9() {
  for (let i = 0; i < students.length; i++) {
    if (students[i].age >= 20 && students[i].age <= 25) {
      console.log(students[i].name);
    }
  }
}

// 10- Añadir un alumno nuevo con los siguientes datos:
// nombre aleatorio.
// edad aleatoria entre 20 y 50 años.
// género aleatorio.
// listado de calificaciones vacío.
// ¡OJO!, el nombre y el género tienen que ir acordes.
function ej10() {
  const newStudent = {};
  newStudent.gender = random_item(availableGenders);
  newStudent.name =
    newStudent.gender === "male"
      ? random_item(availableMaleNames)
      : random_item(availableFemaleNames);
  newStudent.age = calculateRandomNum(20, 50);
  newStudent.examScores = [];
  students.push(newStudent);
}

// 11- Mostrar por consola el nombre de la persona más joven de la clase.
// ¡OJO!, si varias personas de la clase comparten la edad más baja, cualquiera
// de ellos es una respuesta válida.
function ej11() {
  const youngest = students.reduce((a, b) => (a.age < b.age ? a : b));
  console.log(youngest.name);
}

// 12- Mostrar por consola la edad media de todos los alumnos de la clase.
function ej12() {
  const ages = students.map((student) => student.age).reduce((a, b) => a + b);
  console.log(ages / students.length);
}

// 13- Mostrar por consola la edad media de las chicas de la clase.
function ej13() {
  const girls = students.filter(isGirl);
  const ages = girls.map((student) => student.age).reduce((a, b) => a + b);
  console.log(ages / girls.length);
}

// 14- Añadir nueva nota a los alumnos. Por cada alumno de la clase,
// tendremos que calcular una nota de forma aleatoria(número entre 0 y 10) y
// añadirla a su listado de notas.
function ej14() {
  students.forEach((student) => {
    student.examScores.push(calculateRandomNum(0, 10));
  });
}

// // 15- Ordenar el array de alumnos alfabéticamente según su nombre.
function ej15() {
  students.sort((a, b) => (a.name > b.name ? 1 : -1));
}

// Requisitos opcionales
// Os recomiendo encarecidamente que los intentéis, no son difíciles!

// 16- Mostrar por consola el alumno de la clase con las mejores notas.
// El alumno con mejores notas es aquel cuyo sumatorio de todas sus notas
// es el valor más alto de todos.
function sumNotes(student) {
  return student.examScores.reduce((a, b) => a + b);
}

function ej16() {
  console.log(
    students.reduce((a, b) => (sumNotes(a) > sumNotes(b) ? a : b)).name
  );
}

// 17- Mostrar por consola la nota media más alta de la clase y el nombre del
// alumno al que pertenece.
function meanNotes(student) {
  return student.examScores.reduce((a, b) => a + b) / student.examScores.length;
}

function ej17() {
  const student = students.reduce((a, b) =>
    meanNotes(a) > meanNotes(b) ? a : b
  );
  console.log(
    `Nota media mas alta es ${meanNotes(student)} y le pertenece a ${
      student.name
    }`
  );
}

// 18- Añadir un punto extra a cada nota existente de todos los alumnos.
// Recordad que la nota máxima posible es 10. Si los alumnos
// aún no tienen registrada ninguna nota, les pondremos un 10.
function ej18() {
  for (let i = 0; i < students.length; i++) {
    const student = students[i];
    if (student.examScores.length === 0) {
      student.examScores.push(10);
    } else {
      student.examScores = student.examScores.map((score) =>
        Math.min(score + 1, 10)
      );
    }
  }
}

const rl = readline.createInterface(process.stdin, process.stdout);

function getNumberfromConsole() {
  const promise = new Promise((resolve, reject) => {
    rl.question(
      "Ingrese una opción de la 1 a la 18 o 0 para salir\n",
      (num) => {
        rl.pause();
        resolve(num);
      }
    );
  });
  return promise;
}

async function main() {
  let input;
  while (input !== 0) {
    input = await getNumberfromConsole();
    switch (Number(input)) {
      case 1:
        ej1();
        break;
      case 2:
        ej2();
        break;
      case 3:
        ej3();
        break;
      case 4:
        ej4();
        break;
      case 5:
        ej5();
        break;
      case 6:
        ej6();
        break;
      case 7:
        ej7();
        break;
      case 8:
        ej8();
        break;
      case 9:
        ej9();
        break;
      case 10:
        ej10();
        break;
      case 11:
        ej11();
        break;
      case 12:
        ej12();
        break;
      case 13:
        ej13();
        break;
      case 14:
        ej14();
        break;
      case 15:
        ej15();
        break;
      case 16:
        ej16();
        break;
      case 17:
        ej17();
        break;
      case 18:
        ej18();
        break;
      default:
        console.log("Ingrese una opcion valida");
        break;
    }
  }
}

main();
