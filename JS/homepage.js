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
    type1[index].style.marginTop = "12.9%";
    type1[index].style.position = "relative";
    type1[index].style.bottom = "17.5%";
    h1[3 * index].innerHTML = "";
    for (var i = 0; i < hoverPreWeek.length / pre.length; i++) {
        hoverPreWeek[4 * index + i].style.display = "inline-block";
    };
};
function resetPre(index) {
    type1[index].innerHTML = "PRE";
    type1[index].style.marginTop = "17.5%";
    type1[index].style.bottom = "0";
    h1[3 * index].innerHTML = "SEASON";
    for (var i = 0; i < hoverPreWeek.length / pre.length; i++) {
        hoverPreWeek[4 * index + i].style.display = "none";
    };
};

function changeReg(index) {
    type2[index].innerHTML = "WEEK";
    type2[index].style.marginTop = "-9.9%";
    type2[index].style.position = "relative";
    type2[index].style.top = "15%";
    h1[1 + 3 * index].innerHTML = "";
    for (var i = 0; i < hoverRegWeek.length / reg.length; i++) {
        hoverRegWeek[17 * index + i].style.display = "inline-block";
    };
};
function resetReg(index) {
    type2[index].innerHTML = "REGULAR";
    type2[index].style.marginTop = "17.5%";
    type2[index].style.top = "0";
    h1[1 + 3 * index].innerHTML = "SEASON";
    for (var i = 0; i < hoverRegWeek.length / reg.length; i++) {
        hoverRegWeek[17 * index + i].style.display = "none";
    };
};

function changePost(index) {
    type3[index].innerHTML = "ROUND";
    type3[index].style.fontSize = "30px";
    type3[index].style.marginTop = "-14.7%";
    type3[index].style.position = "relative";
    type3[index].style.top = "20%";
    h1[2 + 3 * index].innerHTML = "";
    for (var i = 0; i < hoverPostRound.length / post.length; i++) {
        hoverPostRound[5 * index + i].style.display = "inline-block";
    };
};
function resetPost(index) {
    type3[index].innerHTML = "POST";
    type3[index].style.fontSize = "40px";
    type3[index].style.marginTop = "17.5%";
    type3[index].style.top = "0";
    h1[2 + 3 * index].innerHTML = "SEASON";
    for (var i = 0; i < hoverPostRound.length / post.length; i++) {
        hoverPostRound[5 * index + i].style.display = "none";
    };
};

pre[0].onmouseover = function() {
    changePre(0);
};
pre[0].onmouseout = function() {
    resetPre(0);
};
pre[1].onmouseover = function() {
    changePre(1);
};
pre[1].onmouseout = function() {
    resetPre(1);
};
pre[2].onmouseover = function() {
    changePre(2);
};
pre[2].onmouseout = function() {
    resetPre(2);
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

post[0].onmouseover = function() {
    changePost(0);
};
post[0].onmouseout = function() {
    resetPost(0);
};
post[1].onmouseover = function() {
    changePost(1);
};
post[1].onmouseout = function() {
    resetPost(1);
};
post[2].onmouseover = function() {
    changePost(2);
};
post[2].onmouseout = function() {
    resetPost(2);
};
