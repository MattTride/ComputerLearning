// 1. 找到页面上的按钮和段落（就像在人群中找到特定的人）
const btn = document.getElementById('myBtn');
const msg = document.getElementById('message');

// 2. 定义一个函数：要做什么事？
function handleClick() {
    msg.innerText = "你好！这是由 JavaScript 生成的内容。";
    msg.style.color = "blue"; // 顺便改个颜色
}

// 3. 绑定“监听器”：当按钮被“点击”时，去执行 handleClick 函数
btn.addEventListener('click', handleClick);