var quotes = [];
for (i=0; i<10; i++){
    quotes[i] = "명언 "+ i;
}

var random = Math.floor(Math.random() * 10);
document.write("<p>&quot;" + quotes[random] + "&quot;</p>")
