'use strict';

const year = parseInt(prompt("Enter a year:"), 10);
let isLeap;

if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
  isLeap = true;
} else {
  isLeap = false;
}

const message = isLeap
  ? `${year} is a leap year.`
  : `${year} is not a leap year.`;

document.getElementById("result").textContent = message;