const path = require('path')
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
  res.json({ file: req.file })
})

module.exports = {
  path: '/api/',
  handler: app
}
