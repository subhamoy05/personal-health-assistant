const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// API route to call Flask
app.post('/api/predict', async (req, res) => {
  try {
    const response = await axios.post('http://localhost:8000/predict', {
      symptoms: req.body.symptoms,
    });

    const prediction = response.data.result;
    res.json({ result: prediction });
  } catch (error) {
    console.error('Error connecting to Flask API:', error.message);
    res.status(500).json({ error: 'Flask API error' });
  }
});

app.listen(5000, () => {
  console.log('Node.js server running on http://localhost:5000');
});
