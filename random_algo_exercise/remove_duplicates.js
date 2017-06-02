function RemoveDuplicates(arr){
    var slow = 0;
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] != arr[slow]){
          console.log(arr[slow]);
            slow += 1;
            arr[slow] = arr[i];
        }
    }
    arr.length = slow + 1;
}

arr = [4,4,3,3,2,2,1,1];
RemoveDuplicates(arr);
console.log(arr);
