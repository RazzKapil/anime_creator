
import { useState } from 'react';

export default function Home() {
  const [prompt, setPrompt] = useState('');
  const [userId, setUserId] = useState('user_123');
  const [response, setResponse] = useState(null);

  const handleGenerate = async () => {
    const res = await fetch('/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, user_id: userId })
    });
    const data = await res.json();
    setResponse(data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Script-to-Video</h1>
      <textarea
        rows="4"
        cols="50"
        placeholder="Enter your prompt here..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <br />
      <button onClick={handleGenerate}>Generate Video</button>
      {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
    </div>
  );
}
