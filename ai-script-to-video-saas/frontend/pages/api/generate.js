
export default async function handler(req, res) {
  const { prompt, user_id } = req.body;

  const response = await fetch('http://localhost:8000/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt, user_id })
  });

  const data = await response.json();
  res.status(200).json(data);
}
