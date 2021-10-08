const express = require('express')
const app = express()
const port = 3000

app.get('/login', (req, res) => {
  res.json({
    token: 'secret-key'
  })
})

const loginMiddleware = (req, res, next) => {
  const token = req.headers.authorization;
  if (token != 'secret-key') {
    res.status(403).send("not logged in")
  }
  else {
    next();
  }
}

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/secret', loginMiddleware, (req, res) => {
  res.send('Welcome secret!')
})

app.get('/hello', (req, res) => {
  res.send('Hello!')
})

app.get('/slow', (req, res) => {
  setTimeout(() => {
    res.send('Slow!')
  }, 2000);
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

// curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://192.168.10.103:3000/slow
