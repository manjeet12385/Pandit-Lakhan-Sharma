const fs = require('fs');
let content = fs.readFileSync('astrologer-in-ahmedabad.html', 'utf8');
let match = content.match(/.*? Call \+91/);
if (match) {
    let str = match[0];
    let codes = [];
    for(let i=0; i<str.length; i++) {
        codes.push(str.charCodeAt(i).toString(16));
    }
    console.log(codes.join(' '));
}
