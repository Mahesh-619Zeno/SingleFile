function reverseString(str) {
    return str.split('').reverse().join('');
}

// Example usage
const input = "JavaScript";
const reversed = reverseString(input);

console.log(`Original: ${input}`);
console.log(`Reversed: ${reversed}`);
