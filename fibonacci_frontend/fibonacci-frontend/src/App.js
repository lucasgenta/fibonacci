import React, { useState } from 'react';

function FibonacciCalculator() {
  const [inputValue, setInputValue] = useState('');
  const [result, setResult] = useState('');

  function handleInputChange(event) {
    setInputValue(event.target.value);
  }

  async function calculateFibonacci() {
    const response = await fetch(`/fibonacci?n=${inputValue}`);
    const result = await response.text();
    setResult(result);
  }

  return (
    <div>
      <h1>Fibonacci Calculator</h1>
      <form>
        <label htmlFor="input-n">Enter a number:</label>
        <input type="number" id="input-n" name="n" min="0" value={inputValue} onChange={handleInputChange} />
        <button type="button" onClick={calculateFibonacci}>Calculate</button>
      </form>
      <p>{result ? `Result: ${result}` : ''}</p>
    </div>
  );
}

export default FibonacciCalculator;
