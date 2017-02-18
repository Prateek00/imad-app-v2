var express = require('express');
var morgan = require('morgan');
var path = require('path');

var app = express();
app.use(morgan('combined'));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'index.html'));
});

app.get('/pat',function(req,res){
  res.sendFile(path.join(__dirname, 'ui', 'pat.html'));
});


app.get('/atricle_2',function(req,res){
 res.send('Article two will be served here');    
});

app.get('/atricle_3',function(req,res){
 res.send('Article three will be served here');    
});



app.get('/ui/style.css', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'style.css'));
});

app.get('/ui/main.js', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'main.js'));
});


app.get('/ui/resume.pdf', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'resume.pdf'));
});

app.get('/ui/pat.png', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'pat.png'));
});

app.get('/ui/pat1.jpeg', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'pat1.jpeg'));
});

app.get('/ui/contact.html', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'contact.html'));
});

app.get('/ui/nature.png', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'nature.png'));
});

var port = 8080; // Use 8080 for local development because you might already have apache running on 80
app.listen(8080, function () {
  console.log(`IMAD course app listening on port ${port}!`);
});
