function generateFibonacci(n) {
    if (n <= 0) {
        console.log("Please enter a positive integer.");
        return;
    }

    let a = 0, b = 1;
    const series = [];

    for (let i = 0; i < n; i++) {
        series.push(a);
        [a, b] = [b, a + b]; // Destructuring swap
    }

    console.log("Fibonacci Series:", series.join(" "));
}

// Example usage
const numTerms = 10;
generateFibonacci(numTerms);
