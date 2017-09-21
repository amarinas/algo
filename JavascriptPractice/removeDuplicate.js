// remove duplicate members of an array. create a new array

function removeDuplicate(arr){
  let duplicate = {},
      newArr = [],
      elm;

      for(let i =0; i< arr.length; i++){
        elm = arr[i];
        if(!duplicate[elm]){
          newArr.push(elm);
          duplicate[elm]= true;
        }
      }
      return newArr;
}


console.log(removeDuplicate([1,3,3,3,1,5,6,7,8,1]));
