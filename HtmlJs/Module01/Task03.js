const num1 = parseInt(prompt("Enter the first number:"), 10);
const num2 = parseInt(prompt("Enter the second number:"), 10);
const num3 = parseInt(prompt("Enter the third number:"), 10);

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

document.getElementById("output").innerHTML =
  `Sum: ${sum}<br>Product: ${product}<br>Average: ${average}`;