
import React, { useEffect, useState } from 'react';

const Test = (e) => {
  const [data, setData] = useState({});

  useEffect(() => {
    // Make an API request to the Flask backend
    fetch('/api/Armor')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>{data.name}</h1>
      <p>Age: {data.age}</p>
      <p>City: {data.city}</p>
    </div>
  );
};

export default Test;