const { exec } = require('child_process')

const path = require('path')
const cd = (...p) => path.join(__dirname, path.join(...p))

const { v4: uuidv4 } = require('uuid')

const express = require('express')
const app = express()

const multer = require('multer')
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'static/images')
  },
  filename: (req, file, cb) => {
    cb(null, uuidv4() + path.extname(file.originalname))
  }
})

const uploader = multer({ storage })

app.get('/', (req, res) => {
  // Do
})

app.post('/upload', uploader.single('file'), (req, res) => {
  const file = req.file
  const cmd = `py ${cd('lib/mouth_detection.py')} ${cd('../', file.path)}`
  exec(cmd, (err, stdout, stderr) => {
    res.json({ file, model: JSON.parse(stdout) })
  })
})

module.exports = {
  path: '/api/',
  handler: app
}
