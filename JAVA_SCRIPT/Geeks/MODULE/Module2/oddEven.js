//  nested if statements to check if a number is even or odd and if it is divisible by 4

const readlineSync = require('readline-sync');

const number = Number(readlineSync.question('Please enter a number: '));

console.log(`You entered: ${number}`);

const remainder = number % 2;

if (remainder === 0) {
    console.log('The number is even.');

    if(number % 4 === 0) {
        console.log('The number is also divisible by 4.');
    }else {
        console.log('The number is not divisible by 4.');
    }

}else {
    console.log('The number is odd.');
}