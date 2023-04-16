import React, { useState } from 'react';
import "./MyTest.css";

const MyTest = () => {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [result, setResult] = useState(0);

  const handleAdd = async () => {
    try {
      const response = await fetch('http://localhost:5000/add', {
        method: 'POST',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          num1: num1,
          num2: num2
        })
      });
      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div>
      <h1>Add Two Numbers</h1>
      <input type="number" value={num1} onChange={e => setNum1(Number(e.target.value))} />
      <input type="number" value={num2} onChange={e => setNum2(Number(e.target.value))} />
      <button onClick={handleAdd}>Add</button>
      <p>Result:</p>
      {result !== 0 && <p>{result}</p>}
      
    </div>
  );
};

export default MyTest;