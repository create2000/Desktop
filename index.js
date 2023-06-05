

const http = require('http');


function myServer (req, res) {
   res.write('Hello World'); //write a response to client
   res.end(); //end the response
}

http.createServer(myServer).listen(8080);


const express = require('express');

const app = express()

app.get("/", (req, res)=>{
   res.send("Hello my World, how are you?")
})

const port = 3000
app.listen(port, () => {
   console.log(`Example app listening on port ${port}`)
})



const express = require('express');

const app = express()

app.get("/", (req, res)=>{
   res.sendFile(`${__dirname}/index.html`);
})

const port = 3000
app.listen(port, () => {
   console.log(`Example app listening on port ${port}`)
})

app.use(express.static(__dirname + '/static')) 

//use this for css files and jpegs


const express = require('express');

const app = express()

app.get("/about", (req, res)=>{
   res.sendFile(`${__dirname}/about.html`);
})

const port = 3000
app.listen(port, () => {
   console.log(`Example app listening on port ${port}`)
})
