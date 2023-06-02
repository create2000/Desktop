const express = require('express')
const app = express()
const port = 8080

app.set('view engine', 'pug')

app.get('/', fuction (req, res) {
    res.sendFIle('java.html', {root: __dirname})
});

app.listen(port, (8080))
        /*
        title: 'Hey Express',
    message: 'Hello there',
    expressjs: 'Express JS Framework.' })
})
*/