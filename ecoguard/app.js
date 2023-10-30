// Importe a biblioteca dotenv
const dotenv = require('dotenv');

// Carregue as variáveis de ambiente do arquivo .env
dotenv.config();

// Agora você pode acessar as variáveis de ambiente onde precisar no seu aplicativo
const githubApiKey = process.env.GITHUB_API_KEY;

// Use a variável githubApiKey em seu código
console.log("Sua chave de API do GitHub é: " + githubApiKey);

// Resto do seu código Node.js
// ...
