const firstString = "Hello";
const secondString = "World";
const thirdString = "JavaScript";

if (firstString.length > secondString.length) {

    if(firstString.length > thirdString.length) {
        console.log(`${firstString} is greatest`);
    }else {
        console.log(`${thirdString} is greatest`);
    }

} else {
    if(secondString.length > thirdString.length) {
        console.log(`${secondString} is greatest`);
    }else {
        console.log(`${thirdString} is greatest`);
    }
}

