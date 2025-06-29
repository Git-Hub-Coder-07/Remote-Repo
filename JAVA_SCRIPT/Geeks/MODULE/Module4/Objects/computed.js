/*
computed properties in js
*/

const readlineSync = require("readline-sync");
const userInput = readlineSync.question("Enter the values you want(name/class/roll) :  ");

let obj = {
  name: "Joker",
  class: "10th",
  roll: 1
};


//addind a Property to the object using a variable
obj.grade = "A"; // Adding a new property 'grade' to the object

// Accessing the computed property using the variable userInput
console.log(obj[userInput]); // Output: Joker     (accesing thru computed value)
console.log(obj.class); // Output: 10th     (accesing normal value)
console.log(obj.grade); // Output: A     (accesing normal value)