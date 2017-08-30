//print integers 1 to 100. if divisible by 5 print coding instead. if by 10 also print Dojo

function counting() {
  //iterate from 1 to 100
  for (var i = 1; i <=100; i++) {
    //if current i divisible by 5 == 0 then print coding
    if (i % 5 === 0){
       console.log("Coding");
    // if current i is divisible by 10 then print Dojo. it contunues form the other if
        if (i % 10 === 0 ) {
          console.log("Dojo");
    }
  }
    else {
      console.log(i);
    }
  }
}


console.log(counting());
