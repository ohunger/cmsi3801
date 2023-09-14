const palindromePermutation = (str) => {

    const charMap = new Map(); //frequency of each char in string
    str = str.replace(/\s/g, '').toLowerCase();
    //remove spaces and convert string to lower case

    for (const char of str) {
        if (charMap.has(char)) {
          charMap.set(char, charMap.get(char) + 1);
        } else {
          charMap.set(char, 1);
        }
      }

    //checking palindrome
    let count = 0;
    for (const i of charMap.values()) {
        if (i % 2 !== 0) {
        count++;
        }
    }
    //if one characater with odd freq
    return count <=1;

}
//simple program that counts num of times a character comes up, and then 
// checks if there is less than one character with odd freq, basically
// case of middle character being solo or odd

let test = 'Tact Coa';
console.log(test + " Palindrome: " + palindromePermutation(test));
let test2 = 'Ball'
console.log(test2 + " Palindrome: " + palindromePermutation(test2));