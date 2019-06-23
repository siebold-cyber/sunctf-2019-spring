const cors = require('cors')
const express = require('express')
require('dotenv').config()

const app = express()
app.use(express.json())
app.use(cors())

app.get('/fetchFlag', function (req, res) {
  if(req.get('Bearer') === process.env.BEARER) {
    res.send(JSON.stringify({'flag': process.env.FLAG}))
  } else {
    res.send(JSON.stringify({'flag': 'Access Denied'}))
  }
})

app.listen(8080, () => console.log('Application is runnning on port 8080'))
