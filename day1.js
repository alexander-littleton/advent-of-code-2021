let input = [];

let prev = input[0] + input[1] + input[2];
let increases = 0;
for (let i = 1; i < input.length - 2; i++) {
  let cur = input[i] + input[i + 1] + input[i + 2];
  cur > prev ? increases++ : null;
  prev = cur;
}
console.log(increases);
