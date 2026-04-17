const express = require("express");
const app = express();

// BUG: hardcoded API key
const API_KEY = "sk-proj-abc123def456ghi789jkl012mno345pqrstu678";

// BUG: hardcoded database credentials
const DB_CONFIG = {
  host: "production-db.internal.company.com",
  user: "admin",
  password: "SuperSecret_Passw0rd!2025",
  database: "customers",
};

// BUG: JWT secret in source code
const JWT_SECRET = "my-ultra-secret-jwt-signing-key-do-not-share";

// BUG: AWS credentials exposed
const AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE";
const AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";

app.listen(3000, () => console.log("Server running"));
