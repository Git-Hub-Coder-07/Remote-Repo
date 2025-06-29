/*
function as an object
A function in JavaScript is a first-class object, meaning it can be treated like any other object. This includes being assigned to variables, passed as arguments to other functions, and returned from functions.
*/

let obj = {

  name: "Joker",

  age: 25,

    greet: function() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    },

    bye() {
    console.log(`Goodbye from ${this.name}:)`);
    }

};

//accesing elements of the object
console.log(obj.name); // Output: Joker
console.log(obj.age);  // Output: 25

// Accessing the function as a property of the object
console.log(obj.greet); // Output: [Function: greet]
obj.greet();

console.log(obj.bye);
obj.bye();