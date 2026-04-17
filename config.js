const express = require("express");
const app = express();

// Fixed: API key moved to environment variables
const API_KEY = process.env.OPENAI_API_KEY;

// Fixed: Database credentials moved to environment variables
const DB_CONFIG = {
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
};

// Fixed: JWT secret moved to environment variables
const JWT_SECRET = process.env.JWT_SECRET;

// Fixed: AWS credentials moved to environment variables (or provided via IAM roles)
const AWS_ACCESS_KEY_ID = process.env.AWS_ACCESS_KEY_ID;
const AWS_SECRET_ACCESS_KEY = process.env.AWS_SECRET_ACCESS_KEY;

app.listen(3000, () => console.log("Server running"));