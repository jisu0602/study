var now = new Date();
var firstDay = new Date("2013-06-30");

var toNow = now.getTime();
var toFirst = firstDay.getTime();
var passedDay = Math.round((toNow-toFirst)/(1000*24*60*60));

document.querySelector('#accent').innerText = passedDay + "일";

calcDate(100);
calcDate(200);
calcDate(365);
calcDate(500);

function calcDate(days) {
    var future = toFirst + days*(24*60*60*1000);
    var someday = new Date(future);
    var year = someday.getFullYear();
    var month = someday.getMonth() +1;
    var date = someday.getDate();

    document.querySelector("#date"+days).innerText = year + "년 " + month + "월 " + date + "일";
}