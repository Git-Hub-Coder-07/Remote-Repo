// terniary operator example

const marks = 85;

let result = marks >= 95 ? "A+" :
         marks >= 85 ? "A" :
         marks >= 75 ? "B" :
         marks >= 65 ? "C" :
         marks >= 55 ? "D" :
         "F";

console.log(`Your grade is: ${result}`);