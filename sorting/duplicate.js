function hasDuplicateVal(arr) {
  // presort the array
  arr.sort((a, b) => (a < b) ? -1 : 1);

  //iterate through the values in teh array up until the last one

  for (let i = 0; i < arr.length - 1; i++) {

    // if the val is identical to the next val in the arr, we found a duplicate
    if (arr[i] == arr[i + 1]) {
      return true;
    }
  }

  return false;
}

/*
JS' sort() function has O(N log N) complexity
We iterate through each input val so: (N + log N) + N (N is reduced)
*/