// truthy and falsy values 
// returns the last falsy vcalues

/*
|| is the logical OR operator
It returns the first truthy value or the last falsy value.

&& is the logical AND operator
It returns the first falsy value or the last truthy value.

falsy values - "", 0, null, undefined, NaN, false
truthy values - all other values except falsy values
*/

const firstNAme = "";
const lastName = "Doe";

const userName = firstNAme || lastName;

console.log(userName);