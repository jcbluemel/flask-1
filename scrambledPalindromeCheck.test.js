"use strict";

describe('#scrambledPalindromeCheck', function () {
  it('returns true if string can be made into a palindrome', function () {
    expect(scrambledPalindromeCheck('e')).toBe(true);
    expect(scrambledPalindromeCheck('ee')).toBe(true);
    expect(scrambledPalindromeCheck('bba')).toBe(true);
    expect(scrambledPalindromeCheck("meme")).toBe(true);
    expect(scrambledPalindromeCheck('bbaaa')).toBe(true);
    expect(scrambledPalindromeCheck('cattaco')).toBe(true);
  });

  it('returns false if string cannot be made into a palindrome', function () {
    expect(scrambledPalindromeCheck('ab')).toBe(false);
    expect(scrambledPalindromeCheck('aaabbb')).toBe(false);
    expect(scrambledPalindromeCheck('abc')).toBe(false);
    expect(scrambledPalindromeCheck('cattacox')).toBe(false);
  });
});
