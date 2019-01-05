const pre = document.getElementsByClassName('pre');
const reg = document.getElementsByClassName('reg');
const post = document.getElementsByClassName('post');
const type1 = document.getElementsByClassName('type1');
const type2 = document.getElementsByClassName('type2');
const type3 = document.getElementsByClassName('type3');
const hoverPreWeek = document.getElementsByClassName('hoverPreWeek');
const hoverRegWeek = document.getElementsByClassName('hoverRegWeek');
const hoverPostRound = document.getElementsByClassName('hoverPostRound');
const h1 = document.getElementsByTagName('h1');

function changePre(index) {
    type1[index].innerHTML = "WEEK";
    type1[index].style.top = "0%";
    pre[index].style.position = "absolute";
    reg[index].style.marginLeft = "37.5%";
    h1[3 * index].style.display = "none";
    for (var i = 0; i < hoverPreWeek.length / pre.length; i++) {
        hoverPreWeek[4 * index + i].style.display = "inline-block";
    };
};
function resetPre(index) {
    type1[index].innerHTML = "PRE";
    type1[index].style.top = "25%";
    pre[index].style.position = "relative";
    reg[index].style.marginLeft = "5.75%";
    h1[3 * index].style.display = "block";
    h1[3 * index].style.textAlign = "center";
    for (var i = 0; i < hoverPreWeek.length / pre.length; i++) {
        hoverPreWeek[4 * index + i].style.display = "none";
    };
};

function changeReg(index) {
    type2[index].innerHTML = "WEEK";
    type2[index].style.top = "0%";
    reg[index].style.position = "absolute";
    post[index].style.marginLeft = "37.5%";
    h1[1 + 3 * index].style.display = "none";
    for (var i = 0; i < hoverRegWeek.length / reg.length; i++) {
        hoverRegWeek[17 * index + i].style.display = "inline-block";
    };
};
function resetReg(index) {
    type2[index].innerHTML = "REGULAR";
    type2[index].style.top = "25%";
    reg[index].style.position = "relative";
    post[index].style.marginLeft = "5.75%";
    h1[1 + 3 * index].style.display = "block";
    h1[1 + 3 * index].style.textAlign = "center";
    for (var i = 0; i < hoverRegWeek.length / reg.length; i++) {
        hoverRegWeek[17 * index + i].style.display = "none";
    };
};

function changePost(index) {
    type3[index].innerHTML = "ROUND";
    type3[index].style.top = "0%";
    post[index].style.position = "absolute";
    h1[2 + 3 * index].style.display = "none";
    for (var i = 0; i < hoverPostRound.length / post.length; i++) {
        hoverPostRound[4 * index + i].style.display = "inline-block";
    };
};
function resetPost(index) {
    type3[index].innerHTML = "POST";
    type3[index].style.top = "25%";
    reg[index].style.position = "relative";
    h1[2 + 3 * index].style.display = "block";
    h1[2 + 3 * index].style.textAlign = "center";
    for (var i = 0; i < hoverPostRound.length / post.length; i++) {
        hoverPostRound[4 * index + i].style.display = "none";
    };
};

for (let i = 0; i < pre.length; i++) {
    pre[i].onmouseover = function() {
        changePre(i);
    };
    pre[i].onmouseout = function() {
        resetPre(i);
    };
};

for (let i = 0; i < reg.length; i++) {
    reg[i].onmouseover = function() {
        changeReg(i);
    };
    reg[i].onmouseout = function() {
        resetReg(i);
    };
};

for (let i = 0; i < post.length; i++) {
    post[i].onmouseover = function() {
        changePost(i);
    };
    post[i].onmouseout = function() {
        resetPost(i);
    };
};
