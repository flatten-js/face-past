const express = require('express')
const app = express()

app.get('/', (req, res) => {
  // Do
})

module.exports = {
  path: '/api/',
  handler: app
}
