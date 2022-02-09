"use strict";
/* ------------------------------------------------------------------------------------------------
CHALLENGE 1

Write a function that takes an array of numbers and return a new shuffled array
------------------------------------------------------------------------------------------------ */


const shuffle=(arr,ind)=>{
let arr1=[];

for (let i=0; i< arr.length/2; i++){
  arr1.push(arr[ind+i]);
  arr1.push(arr[i]);

}
return arr1

}

/* ------------------------------------------------------------------------------------------------
CHALLENGE 2

Write a function that takes a binary number and convert it to decimal
------------------------------------------------------------------------------------------------ */

const binToDec=(str)=>{
  let arr1=str.toString().split("")

  let int=0
  let y=0
  for (let i=arr1.length-1; i>=0; i--){

  int+=(arr1[i]*(2**y))
  y++

  }
  return int
  }


/* ------------------------------------------------------------------------------------------------
CHALLENGE 3

Write a function that takes a word and should reverse the word
------------------------------------------------------------------------------------------------ */


  let str = 'i.like.banana';
  //output
  //'banana.like.i'

  function reversedString (str){
    let arr = str.split('.');
    let arr2 = [];
    for(let i = arr.length-1; i >=0; i--){
      arr2.push(arr[i])
    }
    let str2 = arr2.join('.');
    return str2;
  }
  console.log('1. reversedString : ' ,reversedString(str));


/* ------------------------------------------------------------------------------------------------
CHALLENGE 4

Write a function that takes a number and should rearrange it
------------------------------------------------------------------------------------------------ */


function reArrange (n){
  let arr = n.split('') ;
  let n2="";
  while(arr.length>0){
  let pop1=arr.pop();
  let shift1=arr.shift();
  if (  pop1){
  n2+=pop1


  }

  if (shift1  ){
  n2+=shift1;


  }

  }
  return (n2);
}

/* ------------------------------------------------------------------------------------------------
CHALLENGE 5

Write a function that takes a number and should rearrange it
------------------------------------------------------------------------------------------------ */


function duplicateArr (arr){
  let n=arr.length
  for (let i = 0 ; i<n ; i++){
    arr.push(arr[i]);
  }
  return arr;
}


/* ------------------------------------------------------------------------------------------------
CHALLENGE 6

Write a function that takes two numbers and swap it
------------------------------------------------------------------------------------------------ */


function swip (x,y){
  x = x+y;
  y = x-y;
  x = x-y;
  return {'x' : x,'y' : y}
}

/* ------------------------------------------------------------------------------------------------
CHALLENGE 7

Write a function that takes array of numbers and return the repeated one
------------------------------------------------------------------------------------------------ */


function repeatedNum (num){
  let sum = 0;
  for (let i = 0; i< num.length; i++){
    sum+= num[i];
  }
  let result = sum-45;
  return result;
}
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
describe("Testing challenge 1", () => {
  test("It should return a new shuffle array", () => {
    expect(shuffle([4,5,6,8,9,2],3)).toStrictEqual([8,4,9,5,2,6]);
  });
});

describe("Testing challenge 2", () => {
  test("It should convert binary number to decimal number",() => {
    expect(binToDec(1000)).toStrictEqual(8);
  });
});

describe("Testing challenge 3", () => {
  test("It should reverse the array", () => {
    expect(reversedString("i.like.banana")).toStrictEqual("banana.like.i");
  });
});

describe("Testing challenge 4", () => {
  test("It should rearrange the string", () => {
    expect(reArrange("123456 ")).toStrictEqual(" 162534");
  });
});

describe("Testing challenge 5", () => {
  test("It should duplicate the array", () => {
    expect(duplicateArr([1,2,3])).toStrictEqual([1,2,3,1,2,3]);
  });
});

describe("Testing challenge 6", () => {
  test("It should swap the numebrs", () => {
    expect(swip(5,8)).toStrictEqual({"x":8,"y":5});
  });
});



describe("Testing challenge 7", () => {
  test("It should return the rep number", () => {
    expect(repeatedNum([1,2,4,3,5,6,7,8,8,9])).toStrictEqual(8);
  });
});




