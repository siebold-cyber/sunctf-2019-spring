const express = require('express')
require('dotenv').config()

const app = express()

app.use(express.json())

app.get('/', function (req, res) {
  res.append('FLAG', `SUNCTF{${process.env.FLAG}}`)
  res.send('You cannot see the flag!\n')
})

app.listen(8080, () => console.log('Application is running on port 8080'))
