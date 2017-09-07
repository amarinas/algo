// Find all prime factors of a number

function primeFactors(x){
  let factors = [],
      divisor = 2;


  while(x>2){
    if( x % divisor == 0){
        factors.push(divisor);
        x = x / divisor;
    }
    else{
      divisor++;
    }
  }
  return factors;
}

console.log(primeFactors(69));
console.log(primeFactors(120));
