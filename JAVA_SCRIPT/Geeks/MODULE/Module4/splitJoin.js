/*
split and join methods in JavaScript
to check whwther a string entered by the user is palindrome or not
*/

const readlineSync = require("readline-sync");
const userInput = readlineSync.question("Enter a string: ");

// spliiting the string into an array of characters
const charAraay = userInput.split("");
console.log(`The array of characters is: ${charAraay}`);

// reversing the array of characters
const reversedArray = charAraay.reverse();
console.log(`The reversed array of characters is: ${reversedArray}`);

// joining the reversed array back into a string (no use of join method here)
const reversedString = reversedArray.join("");

// checking if the original string is equal to the reversed string
if (userInput === reversedString) {
  console.log(`The string "${userInput}" is a palindrome.`);
} else {
  console.log(`The string "${userInput}" is not a palindrome.`);
}