var button = document.getElementById('counter');

var counter = 0;
button.onclick = fumction(){
    
    counter = counter + 1;
    var span = document.getElementById('count');
    span.innerHTML = counter.toString();
};