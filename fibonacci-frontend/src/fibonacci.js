import React, { useState } from "react";

function Fibonacci() {
  const [result, setResult] = useState("");
  const [input, setInput] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch(`http://167.71.41.144:5000/fibonacci?n=${input}`);
    const data = await response.text();
    setResult(data);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Enter a number:
          <input type="number" value={input} onChange={(e) => setInput(e.target.value)} />
        </label>
        <button type="submit">Submit</button>
      </form>
      <p>Result: {result}</p>
    </div>
  );
}

export default Fibonacci;
