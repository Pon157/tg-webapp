module.exports = {
  apps: [{
    name: 'tma-backend',
    script: './backend/index.js',
    env: {
      NODE_ENV: 'production',
    }
  }]
}
