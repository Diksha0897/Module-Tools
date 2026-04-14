const fs = require("fs");
const glob = require("glob");

const args = process.argv.slice(2);

let numberLines = false;
let numberNonEmpty = false;
let files = [];

// Parse arguments
for (let arg of args) {
  if (arg === "-n") {
    numberLines = true;
  } else if (arg === "-b") {
    numberNonEmpty = true;
  } else {
    // expand glob patterns
    const matches = glob.sync(arg);
    if (matches.length > 0) {
      files.push(...matches);
    } else {
      files.push(arg);
    }
  }
}

// -b overrides -n
if (numberNonEmpty) {
  numberLines = false;
}

let lineNumber = 1;

for (let file of files) {
  try {
    const content = fs.readFileSync(file, "utf-8");
    const lines = content.split("\n");

    for (let line of lines) {
      if (numberNonEmpty) {
        if (line.trim() !== "") {
          console.log(`${lineNumber++} ${line}`);
        } else {
          console.log("");
        }
      } else if (numberLines) {
        console.log(`${lineNumber++} ${line}`);
      } else {
        console.log(line);
      }
    }
  } catch (err) {
    console.error(`cat: ${file}: ${err.message}`);
  }
}
