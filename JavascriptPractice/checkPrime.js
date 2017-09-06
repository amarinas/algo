//check a number if it is a prime number return true or false

function isPrime(n){
  let divisor = 2;

  while(n > divisor){
    if(n % divisor == 0){
      return false;
    }
    else
      divisor++;
    }
    return true;
  }




console.log(isPrime(137));
console.log(isPrime(237));
console.log(isPrime(409));
console.log(isPrime(349));
