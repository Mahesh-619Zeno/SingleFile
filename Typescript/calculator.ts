function calculate(a: number, b: number, op: string, log: boolean = false): number | string {
    let result: number | string;

    switch (op) {
        case '+': result = a + b; break;
        case '-': result = a - b; break;
        case '*': result = a * b; break;
        case '/': result = b !== 0 ? a / b : 'Undefined'; break;
        default: result = 'Invalid'; break;
    }

    if (log) {
        console.log(`Calculated: ${a} ${op} ${b} = ${result}`);
    }

    return result;
}

// Optional variable with explicit type
let debugMode: boolean = true;
let mode: boolean = false; 

const a: number = parseFloat(prompt("Enter first number:") || '0');
const b: number = parseFloat(prompt("Enter second number:") || '0');
const op: string = prompt("Enter operation (+ - * /):") || '+';

alert("Result: " + calculate(a, b, op, debugMode));
