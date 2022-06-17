"use strict";

/** Returns frequency counter for each letter in given word */

function createFreqCounter(word) {

  const counter = {};

  for (let ltr of word) {
    counter[ltr] = (counter[ltr] || 0) + 1;
  }

  return counter;
}

/** Returns true if letters in word can be rearranged to create a palindrome.
 *  Else returns false.
 */

function scrambledPalindromeCheck(word) {

  const ltrToCounts = createFreqCounter(word);
  let oddCount = false;

  for (let ltr in ltrToCounts) {

    if (ltrToCounts[ltr] % 2 === 1) {
      if (oddCount) {
        return false;
      } else {
        oddCount = true;
      }
    }
  }

  return true;
}

