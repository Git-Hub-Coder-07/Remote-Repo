inputString = "GeeksforGeeks is a computer science portal for geeks";
vowels = "aeiouAEIOU";

for (let i=0; i<inputString.length; i++){
    if(vowels.includes(inputString[i])) {
        console.log(`${inputString[i]} is a vowel`);
    }
}