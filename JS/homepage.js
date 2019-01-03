const regular = document.getElementsByClassName('reg');

for (var i = 0; i < regular.length; i++) {
    console.log(i);
    regular[i].onmouseover = function() {
        regular[i].style.backgroundColor = "blue";
    };
};
