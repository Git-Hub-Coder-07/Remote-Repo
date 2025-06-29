const availableSizes = ['S', 'M', 'L', 'XL', 'XXL'];

const readlineSync = require('readline-sync');

const userInput = readlineSync.question('Enter a size (S, M, L, XL, XXL, XXXL): ');

if (availableSizes.includes(userInput)) {
  console.log(`The size ${userInput} is available.`);
} else {
  console.log(`The size ${userInput} is not available.`);
}