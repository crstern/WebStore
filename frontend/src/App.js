import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);

  return (
    <div>
      {data}
    </div>
  );
}

export default App;