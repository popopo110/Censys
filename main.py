const API = 'https://<your-backend-host>.onrender.com'; // <-- replace

async function run() {
  const records = /* array of host objects */;
  const model = 'gpt-4o-mini';
  const temperature = 0.2;

  const res = await fetch(`${API}/api/summarize-batch`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ records, model, temperature })
  });

  const text = await res.text();
  const data = JSON.parse(text); // show errors if parse fails
  console.log(data);
}
