// Set myNumber to 42. set myName to your name. now swap myNumber into myName and vice versa


var myNumber = 42;
var myName = "Ali";
console.log("original myNumber", myNumber);
console.log("original myName", myName);
var temp = myNumber;

myNumber = myName;
myName = temp;

console.log("my number after switch", myNumber);
console.log("my name after switch",  myName);
