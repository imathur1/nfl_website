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

for (let i = 0; i < line.length; i++) {
    line[i].onmouseover = function() {
        line[i].style.color = "#00ffbc";
        line[i].style.cursor = "pointer";
        line[i].onclick = function() {
            window.scroll({
               top: 450 * i,
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
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/49erWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/bearWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/bengalWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/billWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/broncoWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/brownWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/buccaneerWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/cardinalWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/coltWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/chiefWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/chargerWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/cowboyWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/dolphinWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/eagleWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/giantWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/jaguarWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/falconWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/jetWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/packerWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/lionWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/patriotWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/pantherWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/raiderWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/redskinWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/saintWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/seahawkWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/ravenWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/ramWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/texanWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/titanWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/vikingWallpaper.png",
    "/Users/ishaan/Coding/Projects/NFL_Website/Images/steelerWallpaper.png"
];

var previous = -1;
for (var i = 0; i < everyTwo.length; i++){
    var random = Math.floor(Math.random() * 32);
    while (random === previous) {
        random = Math.floor(Math.random() * 32);
    };
    everyTwo[i].style.background = 'linear-gradient(rgba(255,255,255,.2), rgba(255,255,255,.2)), url(' + wallpapers[random] + ')';
    previous = random;
};

function changePre(index) {
    type1[index].innerHTML = "WEEK";
    type1[index].style.top = "0%";
    pre[index].style.position = "absolute";
    pre[index].style.height = "3.07%";
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
    pre[index].style.height = "32.5%";
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
    reg[index].style.height = "3.07%";
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
    reg[index].style.height = "32.5%";
    h1[1 + 3 * index].style.display = "block";
    h1[1 + 3 * index].style.textAlign = "center";
    for (var i = 0; i < hoverRegWeek.length / reg.length; i++) {
        hoverRegWeek[17 * index + i].style.display = "none";
    };
};

function changePost(index) {
    type3[index].innerHTML = "ROUND";
    type3[index].style.top = "0%";
    post[index].style.height = "3.07%";
    post[index].style.position = "absolute";
    h1[2 + 3 * index].style.display = "none";
    for (var i = 0; i < hoverPostRound.length / post.length; i++) {
        hoverPostRound[4 * index + i].style.display = "inline-block";
    };
};
function resetPost(index) {
    type3[index].innerHTML = "POST";
    type3[index].style.top = "25%";
    post[index].style.position = "relative";
    post[index].style.height = "32.5%";
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
