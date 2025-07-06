// var p= new Promise(function(){
//     return "OK";
// });

// var p2 = p.then(function(data){
//     return data;
// });

// var p3 = p2.then(function(data){
//     return data+"Bye";
// });

// var book = {"main title":"JAvaScript", 
//     'subtitle':"the defentive guide",
//     "for":"all audience",
//     author:{
//         firstname:"Rahul",
//         surname:"Sharma"
//     }
// };

// let chaval= (p)=>p+2;
// console.log(chaval(2));

// var p = new Promise(function(resolve,reject){
//     setTimeout(function(){
//         resolve("OK");
//     }, 2000);
// });

// p.then().then(function(data){
//     console.log(data);
// });

// var text = "texting: 1,2,3";
// var pattern = /d+/g

// num1=5;
// function cal() {
// num1=10;
// num2=5;
// num3=num2*num1;
// console.log(num3);
// }
// cal();

var p = new Promise(function(resolve, reject) {
  setTimeout(function() {
    resolve("OK");
  }, 2000);
});

var p2 = p.then(function(data) {
  return data + " Good";
});