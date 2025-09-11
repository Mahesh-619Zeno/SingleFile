function isPalindrome(str) {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    const reversed = cleaned.split('').reverse().join('');
    return cleaned === reversed;
}

// Example usage
const input = "Madam";
if (isPalindrome(input)) {
    console.log(`"${input}" is a palindrome.`);
} else {
    console.log(`"${input}" is not a palindrome.`);
}
