const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');
require('dotenv').config();

const app = express();
const pool = new Pool({ connectionString: process.env.DATABASE_URL });

app.use(cors());
app.use(express.json());

// Получение списка проектов, отсортированных по score
app.get('/api/projects', async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM projects ORDER BY score DESC');
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.listen(process.env.PORT, () => console.log(`API running on port ${process.env.PORT}`));
