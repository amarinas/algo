//Using a FOR loop, print multiples of 3  from -300 to 0 skip -3 and -6

function multipleOfThree() {
  for (var i = -300; i <= 0; i+=3) {
    if(i === -3 || i ===-6){
      continue;
    }
    console.log(i);
  }
}



console.log(multipleOfThree());
