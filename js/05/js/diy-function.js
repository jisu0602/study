var num1 = parseInt(prompt("첫 번째 숫자 입력"));
var num2 = parseInt(prompt("두 번째 숫자 입력"));
var result = add(num1, num2);
alert(num1+" 더하기 "+num2+"은/는 "+result+"입니다.")


function add(a, b){
    var sum = a + b;
    return sum;
}