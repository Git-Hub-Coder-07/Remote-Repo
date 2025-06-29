let s = "madama"; // You can change this string to test other cases
let flag =false;
for( let i=0, j=s.length-1 ; i<=j ; i++,j--){
    if(s[i]===s[j]){
        flag = true;
    }else{
        flag = false;
        break;
    }
}
        
if (flag){
    console.log("Palindrome");
}else{
    console.log("Not Palindrome");
}
    