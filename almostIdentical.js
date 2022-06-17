"use strict";

/** Given two strings, find if they are, at most, a single edit away from
 *  being identical. An edit is adding, deleting, or changing a single letter.
 *  Returns true if so, false if not.
*/

function almostIdentical(s1, s2) {

  let diffLen = Math.abs(s1.length - s2.length);
  if (diffLen > 1) return false;
  if (diffLen === 0) return checkDiffWithSameLength(s1, s2);

  const lengthOrder = orderStrByLength(s1, s2);
  let longer = lengthOrder[0];
  let shorter = lengthOrder[1];

  return checkDiffWithDiffLength(longer, shorter);
}


/** Takes input strings and returns them ordered by length [long, short] */

function orderStrByLength(s1, s2) {

  if (s1.length > s2.length) return [s1, s2];

  return [s2, s1];
}

/** Check how many differences exist between strings of same length.
 *  Return true if less than 2 differences found, otherwise false.
 */

function checkDiffWithSameLength(s1, s2) {

  let diffFound = false;
  for (let i = 0; i < s1.length; i++) {

    if (s1[i] !== s2[i]) {
      if (diffFound === true) return false;
      else diffFound = true;
    }
  }

  return true;
}

/** Converts given strings into arrays.
 *  Loops through longer array, and removes first difference found between
 *  them from the longer array.
 *  Return true if resulting arrays are identical, otherwise false.
 */

function checkDiffWithDiffLength(longerS, shorterS) {

  let longerA = longerS.split("");
  let shorterA = shorterS.split("");

  for (let i = 0; i < longerA.length; i++) {

    if (longerA[i] !== shorterA[i]) {
      longerA.splice(i, 1);
      break;
    }
  }

  return longerA.every((ltr, idx) => shorterA[idx] === ltr);
}