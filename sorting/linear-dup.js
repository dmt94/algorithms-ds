function hasDuplicateVal(arr) {
  let existingNums = [];
  for (let i = 0; i < arr.length; i++) {
    if(existingNums[arr[i]] === 1) {
      return true;
    } else {
      existingNums[arr[i]] = 1;
    }
  }
  return false;
}

console.log(hasDuplicateVal([3,4,2,3]))

console.log(undefined === 1);