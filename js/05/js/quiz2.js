var num1 = parseInt(prompt("비교할 첫 번째 숫자를 입력해주세용."));
var num2 = parseInt(prompt("두 번째 숫자를 입력해주세용."));
compareNum(num1, num2);

function compareNum(a, b) {
    if (a > b) alert(a+"(이)가 "+b+"보다 큽니다.");
    else if (a < b) alert(b+"(이)가 "+a+"보다 큽니다.");
    else alert("두 숫자는 같습니다.");
}