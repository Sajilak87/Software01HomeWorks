'use strict';

const name = prompt("Enter your name:");
const randomNum = Math.floor(Math.random() * 4) + 1;
let house;

switch (randomNum) {
  case 1:
    house = "Gryffindor";
    break;
  case 2:
    house = "Slytherin";
    break;
  case 3:
    house = "Hufflepuff";
    break;
  case 4:
    house = "Ravenclaw";
    break;
}

document.getElementById("result").textContent = `${name}, you are ${house}.`;