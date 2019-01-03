const pre = document.getElementsByClassName('pre');
const reg = document.getElementsByClassName('reg');
const post = document.getElementsByClassName('post');
const type1 = document.getElementsByClassName('type1');
const type2 = document.getElementsByClassName('type2');
const type3 = document.getElementsByClassName('type3');
const h1 = document.getElementsByTagName('h1');

function changeReg(index) {
    type2[index].innerHTML = "WEEK";
    type2[index].style.position = "relative";
    type2[index].style.bottom = "20%";
    h1[1 + 3 * index].style.color = "#000";
};

function resetReg(index) {
    type2[index].innerHTML = "REGULAR";
    type2[index].style.bottom = "0";
    h1[1 + 3 * index].style.color = "#fff";
};

reg[0].onmouseover = function() {
    changeReg(0);
};
reg[0].onmouseout = function() {
    resetReg(0);
};

reg[1].onmouseover = function() {
    changeReg(1);
};
reg[1].onmouseout = function() {
    resetReg(1);
};

reg[2].onmouseover = function() {
    changeReg(2);
};
reg[2].onmouseout = function() {
    resetReg(2);
};
