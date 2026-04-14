const fs = require("fs");
const args = process.argv.slice(2);

let showL = false;
let showW = false;
let showC = false;
let files = [];

// parse args (supports -lwc style too)
for (let arg of args) {
  if (arg.startsWith("-") && arg.length > 1) {
    for (let ch of arg.slice(1)) {
      if (ch === "l") showL = true;
      else if (ch === "w") showW = true;
      else if (ch === "c") showC = true;
    }
  } else {
    files.push(arg);
  }
}

// default: show all if no flags given
if (!showL && !showW && !showC) {
  showL = showW = showC = true;
}

// word count (GNU wc style)
function countWords(str) {
  const match = str.match(/\S+/g);
  return match ? match.length : 0;
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (let file of files) {
  try {
    const buffer = fs.readFileSync(file);
    const content = buffer.toString("utf8");

    const bytes = buffer.length;

    // line count = number of newline characters
    const lines = content.length === 0 ? 0 : content.split("\n").length - 1;

    const words = countWords(content);

    totalLines += lines;
    totalWords += words;
    totalBytes += bytes;

    let output = [];

    if (showL) output.push(lines);
    if (showW) output.push(words);
    if (showC) output.push(bytes);

    output.push(file);

    console.log(output.join(" "));
  } catch (err) {
    console.error(`wc: ${file}: ${err.message}`);
  }
}

// totals for multiple files
if (files.length > 1) {
  let total = [];

  if (showL) total.push(totalLines);
  if (showW) total.push(totalWords);
  if (showC) total.push(totalBytes);

  total.push("total");

  console.log(total.join(" "));
}
