const { PDFParse } = require('./node_modules/pdf-parse');
const fs = require('fs');
const buf = fs.readFileSync('design/Datasheets/RPi-cm5-design-guide.pdf');
const parser = new PDFParse();
parser.parse(buf).then(data => {
  const text = data.text;
  const keywords = ['power button', 'PWR_BTN', 'GLOBAL_EN', 'GLOBAL EN', 'POWER GOOD', 'PWR_GD', 'power good', 'nRUN', 'RUN pin', 'PWRKEY', 'power key', 'graceful', 'halt', 'shutdown'];
  const results = [];
  keywords.forEach(kw => {
    let idx = text.toLowerCase().indexOf(kw.toLowerCase());
    if (idx >= 0) {
      results.push('=== Found: [' + kw + '] ===');
      results.push(text.substring(Math.max(0,idx-200), idx+500));
      results.push('---');
    }
  });
  fs.writeFileSync('C:/Users/izzyo/AppData/Local/Temp/cm5-pdf-search.txt', results.join('\n'));
  console.log('Done, found', results.length, 'result blocks, total text chars:', text.length);
}).catch(e => { console.error('ERROR:', e.message); });
