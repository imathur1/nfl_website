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
const everyTwo = document.getElementsByClassName('everyTwo');
const year = document.getElementsByClassName('year');
const home = document.getElementsByClassName('home');
const season = document.getElementsByClassName('season');
const dropdown = document.getElementsByClassName('dropdown');
const line = document.getElementsByClassName('line');
const nav = document.getElementsByClassName('nav');

home[0].onmouseover = function() {
    home[0].style.color = "#00ffbc";
};

home[0].onmouseout = function() {
    home[0].style.color = "#fff";
};
home[0].onclick = function() {
    window.scroll({
       top: 0,
       left: 0,
       behavior: 'smooth'
    });
};

season[0].onmouseover = function() {
    season[0].style.color = "#00ffbc";
    dropdown[0].style.display = "block";
};
dropdown[0].onmouseover = function() {
    season[0].style.color = "#00ffbc";
    dropdown[0].style.display = "block";
};
dropdown[0].onmouseout = function() {
    dropdown[0].style.display = "none";
    season[0].style.color = "#fff";
};
nav[0].onmouseout = function() {
    dropdown[0].style.display = "none";
    season[0].style.color = "#fff";
};

for (let i = 0; i < line.length; i++) {
    line[i].onmouseover = function() {
        line[i].style.color = "#00ffbc";
        line[i].style.cursor = "pointer";
        line[i].onclick = function() {
            window.scroll({
               top: (screen.height * 0.5) * i,
               left: 0,
               behavior: 'smooth' 
            });
        };
    };
    line[i].onmouseout = function() {
        line[i].style.color = "#fff";
    };
};

const wallpapers = [
    "../Images/49erWallpaper.png",
    "../Images/bearWallpaper.png",
    "../Images/bengalWallpaper.png",
    "../Images/billWallpaper.png",
    "../Images/broncoWallpaper.png",
    "../Images/brownWallpaper.png",
    "../Images/buccaneerWallpaper.png",
    "../Images/cardinalWallpaper.png",
    "../Images/coltWallpaper.png",
    "../Images/chiefWallpaper.png",
    "../Images/chargerWallpaper.png",
    "../Images/cowboyWallpaper.png",
    "../Images/dolphinWallpaper.png",
    "../Images/eagleWallpaper.png",
    "../Images/giantWallpaper.png",
    "../Images/jaguarWallpaper.png",
    "../Images/falconWallpaper.png",
    "../Images/jetWallpaper.png",
    "../Images/packerWallpaper.png",
    "../Images/lionWallpaper.png",
    "../Images/patriotWallpaper.png",
    "../Images/pantherWallpaper.png",
    "../Images/raiderWallpaper.png",
    "../Images/redskinWallpaper.png",
    "../Images/saintWallpaper.png",
    "../Images/seahawkWallpaper.png",
    "../Images/ravenWallpaper.png",
    "../Images/ramWallpaper.png",
    "../Images/texanWallpaper.png",
    "../Images/titanWallpaper.png",
    "../Images/vikingWallpaper.png",
    "../Images/steelerWallpaper.png"
];

var previous = -1;
for (var i = 0; i < everyTwo.length; i++){
    var random = Math.floor(Math.random() * 32);
    while (random === previous) {
        random = Math.floor(Math.random() * 32);
    };
    everyTwo[i].style.background = 'linear-gradient(rgba(255,255,255,.2), rgba(255,255,255,.2)), url(' + wallpapers[random] + ')';
    everyTwo[i].style.backgroundSize = "cover";
    previous = random;
};

function changePre(index) {
    type1[index].innerHTML = "WEEK";
    type1[index].style.marginTop = "0%";
    pre[index].style.position = "absolute";
    reg[index].style.marginLeft = "37%";
    h1[3 * index].style.display = "none";
    for (var i = 0; i < hoverPreWeek.length / pre.length; i++) {
        hoverPreWeek[4 * index + i].style.display = "inline-block";
    };
};
function resetPre(index) {
    type1[index].innerHTML = "PRE";
    type1[index].style.marginTop = "22.5%";
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
    type2[index].style.marginTop = "0%";
    reg[index].style.position = "absolute";
    post[index].style.marginLeft = "37%";
    h1[1 + 3 * index].style.display = "none";
    for (var i = 0; i < hoverRegWeek.length / reg.length; i++) {
        hoverRegWeek[17 * index + i].style.display = "inline-block";
    };
};
function resetReg(index) {
    type2[index].innerHTML = "REGULAR";
    type2[index].style.marginTop = "22.5%";
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
    type3[index].style.marginTop = "0%";
    post[index].style.position = "absolute";
    h1[2 + 3 * index].style.display = "none";
    for (var i = 0; i < hoverPostRound.length / post.length; i++) {
        hoverPostRound[4 * index + i].style.display = "inline-block";
    };
};
function resetPost(index) {
    type3[index].innerHTML = "POST";
    type3[index].style.marginTop = "22.5%";
    post[index].style.position = "relative";
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