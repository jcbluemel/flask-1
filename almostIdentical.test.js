"use strict";

describe("#almostIdentical", function() {
  it("returns true for words of the same length at most one edit away", function() {
    expect(almostIdentical("make", "make")).toBe(true);
    expect(almostIdentical("make", "fake")).toBe(true);
  });
  
  it("returns false for words of the same length more than one edit away", function() {
    expect(almostIdentical("task", "take")).toBe(false);
    expect(almostIdentical("shoe", "hose")).toBe(false);
  });

  it("returns true for words of different length at most one edit away", function() {
    expect(almostIdentical("ask", "asks")).toBe(true);
    expect(almostIdentical("asks", "ask")).toBe(true);
    expect(almostIdentical("act", "tact")).toBe(true);
    expect(almostIdentical("tact", "act")).toBe(true);
    expect(almostIdentical("fat", "fact")).toBe(true);
  });

  it("returns false for words of different length more than one edit away", function() {
    expect(almostIdentical("yes", "no")).toBe(false);
    expect(almostIdentical("tile", "liter")).toBe(false);
    expect(almostIdentical("short", "longerthanshort")).toBe(false);
  });
});