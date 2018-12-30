const name1 = document.getElementsByClassName('name1');
const name2 = document.getElementsByClassName('name2');
const score1 = document.getElementsByClassName('score1');
const score2 = document.getElementsByClassName('score2');
const teamName = document.getElementsByClassName('team-name');
const teamName1 = document.getElementsByClassName('team-name1');
const teamName2 = document.getElementsByClassName('team-name2');
const result = document.getElementsByClassName('result');
const date = document.getElementsByClassName('date');
const record1 = document.getElementsByClassName('record1');
const record2 = document.getElementsByClassName('record2');
const quarter = document.getElementsByClassName('quarter');
const quarter1 = document.getElementsByClassName('quarter1');
const quarter2 = document.getElementsByClassName('quarter2');
const quarterHidden = document.getElementsByClassName('quarter-hidden');

const standings = [
['Arizona Cardinals', [3, 12, 0]],
['Atlanta Falcons', [6, 9, 0]],
['Baltimore Ravens', [9, 6, 0]],
['Buffalo Bills', [5, 10, 0]],
['Carolina Panthers', [6, 9, 0]],
['Chicago Bears', [11, 4, 0]],
['Cincinnati Bengals', [6, 9, 0]],
['Cleveland Browns', [7, 7, 1]],
['Dallas Cowboys', [9, 6, 0]],
['Denver Broncos', [6, 9, 0]],
['Detroit Lions', [5, 10, 0]],
['Green Bay Packers', [6, 8, 1]],
['Houston Texans', [10, 5, 0]],
['Indianapolis Colts', [9, 6, 0]],
['Jacksonville Jaguars', [5, 10, 0]],
['Kansas City Chiefs', [11, 4, 0]],
['Los Angeles Chargers', [11, 4, 0]],
['Los Angeles Rams', [12, 3, 0]],
['Miami Dolphins', [7, 8, 0]],
['Minnesota Vikings', [8, 6, 1]],
['New England Patriots', [10, 5, 0]],
['New Orleans Saints', [13, 2, 0]],
['New York Giants', [5, 10, 0]],
['New York Jets', [4, 11, 0]],
['Oakland Raiders', [4, 11, 0]],
['Philadelphia Eagles', [8, 7, 0]],
['Pittsburgh Steelers', [8, 6, 1]],
['San Francisco 49ers', [4, 11, 0]],
['Seattle Seahawks', [9, 6, 0]],
['Tampa Bay Buccaneers', [5, 10, 0]],
['Tennessee Titans', [9, 6, 0]],
['Washington Redskins', [7, 8, 0]]];

const info = [
[['Tennessee Titans', 25, [6, 3, 0, 16, 25]], ['Washington Redskins', 16, [3, 7, 3, 3, 16]], [736922, 'Sat, 22/12']],
[['New Orleans Saints', 31, [7, 10, 7, 7, 31]], ['Pittsburgh Steelers', 28, [3, 11, 14, 0, 28]], [736923, 'Sun, 23/12']],
[['Detroit Lions', 9, [3, 6, 0, 0, 9]], ['Minnesota Vikings', 27, [0, 14, 3, 10, 27]], [736923, 'Sun, 23/12']],
[['Carolina Panthers', 10, [7, 3, 0, 0, 10]], ['Atlanta Falcons', 24, [7, 3, 14, 0, 24]], [736923, 'Sun, 23/12']],
[['Los Angeles Chargers', 10, [0, 3, 7, 0, 10]], ['Baltimore Ravens', 22, [3, 3, 10, 6, 22]], [736923, 'Sun, 23/12']],
[['Indianapolis Colts', 28, [0, 7, 14, 7, 28]], ['New York Giants', 27, [14, 3, 7, 3, 27]], [736923, 'Sun, 23/12']],
[['New York Jets', 38, [7, 14, 14, 3, 38, 0]], ['Green Bay Packers', 44, [0, 17, 3, 18, 44, 6]], [736923, 'Sun, 23/12']],
[['Dallas Cowboys', 27, [14, 3, 10, 0, 27]], ['Tampa Bay Buccaneers', 20, [3, 10, 0, 7, 20]], [736923, 'Sun, 23/12']],
[['Arizona Cardinals', 9, [3, 6, 0, 0, 9]], ['Los Angeles Rams', 31, [7, 14, 3, 7, 31]], [736923, 'Sun, 23/12']],
[['Cleveland Browns', 26, [0, 16, 7, 3, 26]], ['Cincinnati Bengals', 18, [0, 0, 0, 18, 18]], [736923, 'Sun, 23/12']],
[['New England Patriots', 24, [7, 7, 7, 3, 24]], ['Buffalo Bills', 12, [0, 0, 6, 6, 12]], [736923, 'Sun, 23/12']],
[['Philadelphia Eagles', 32, [7, 6, 10, 9, 32]], ['Houston Texans', 30, [0, 16, 0, 14, 30]], [736923, 'Sun, 23/12']],
[['Miami Dolphins', 7, [7, 0, 0, 0, 7]], ['Jacksonville Jaguars', 17, [7, 0, 0, 10, 17]], [736923, 'Sun, 23/12']],
[['San Francisco 49ers', 9, [0, 9, 0, 0, 9]], ['Chicago Bears', 14, [0, 7, 7, 0, 14]], [736923, 'Sun, 23/12']],
[['Seattle Seahawks', 38, [7, 7, 10, 14, 38]], ['Kansas City Chiefs', 31, [3, 7, 7, 14, 31]], [736924, 'Mon, 24/12']],
[['Oakland Raiders', 27, [7, 10, 0, 10, 27]], ['Denver Broncos', 14, [0, 0, 7, 7, 14]], [736925, 'Tue, 25/12']]];

let count = 0;
for (let i = 0; i < name1.length; i++){
    date[i].innerHTML = info[i][2][1];
    name1[i].innerHTML = info[i][0][0];  
    name2[i].innerHTML = info[i][1][0];
    score1[i].innerHTML = info[i][0][1];  
    score2[i].innerHTML = info[i][1][1];
    
    for (let j = 0; j < standings.length; j++){
        if (standings[j][0] === name1[i].innerHTML){
            if (standings[j][1][2] === 0){
                record1[i].innerHTML = "(" + standings[j][1][0] + " - " + standings[j][1][1] + ")";
            } else {
                record1[i].innerHTML = "(" + standings[j][1][0] + " - " + standings[j][1][1] + " - " + standings[j][1][2] + ")";
            };
        } else if (standings[j][0] === name2[i].innerHTML) {
            if (standings[j][1][2] === 0){
                record2[i].innerHTML = "(" + standings[j][1][0] + " - " + standings[j][1][1] + ")";
            } else {
                record2[i].innerHTML = "(" + standings[j][1][0] + " - " + standings[j][1][1] + " - " + standings[j][1][2] + ")";
            };
        };
    };
    
    teamName1[i].innerHTML = info[i][0][0]; 
    teamName2[i].innerHTML = info[i][1][0]; 
    let overtime = false;
    let value = info[i][0][2].length;
    if (value === 6){
        result[count].innerHTML = 'Final/OT';
        overtime = true;
        for (let k = 0; k < value - 1; k++){
            quarter[i * 5 + k].style.left = "2.5%";
            quarter1[i * 5 + k].style.left = "2.5%";
            quarter2[i * 5 + k].style.left = "2.5%";
            teamName[i].style.right = "3.5%";
            teamName1[i].style.right = "3.5%";
            teamName2[i].style.right = "3.5%";
            if (k === 3){
                quarterHidden[i * 3].style.display = "inline-block";
                quarterHidden[i * 3].style.position = "relative";
                quarterHidden[i * 3].style.left = "2.5%";
                quarterHidden[i * 3 + 1].style.display = "inline-block";
                quarterHidden[i * 3 + 1].style.position = "relative";
                quarterHidden[i * 3 + 1].style.left = "2.5%";
                quarterHidden[i * 3 + 1].innerHTML = info[i][0][2][5];
                quarterHidden[i * 3 + 2].style.display = "inline-block";
                quarterHidden[i * 3 + 2].style.position = "relative";
                quarterHidden[i * 3 + 2].style.left = "2.5%";
                quarterHidden[i * 3 + 2].innerHTML = info[i][1][2][5];   
            };
        };
    };
    count += 1;

    let temp = 0;
    if (overtime === true){
        temp = 1;
    };

    if (Number(score1[i].innerHTML) > Number(score2[i].innerHTML)){
        name1[i].style.color = "#00ffbc"; 
        score1[i].style.color = "#00ffbc";
        teamName1[i].style.color = "#00ffbc";
        for (let k = 0; k < value - temp; k++){
            quarter1[i * 5 + k].style.color = "#00ffbc";
            quarter1[i * 5 + k].innerHTML = info[i][0][2][k];
            quarter2[i * 5 + k].innerHTML = info[i][1][2][k];
            quarterHidden[i * 3 + 1].style.color = "#00ffbc";
        };
        
    } else if (Number(score1[i].innerHTML) < Number(score2[i].innerHTML)){
        name2[i].style.color = "#00ffbc";
        score2[i].style.color = "#00ffbc";
        teamName2[i].style.color = "#00ffbc";
        for (let k = 0; k < value - temp; k++){
            quarter2[i * 5 + k].style.color = "#00ffbc";
            quarter2[i * 5 + k].innerHTML = info[i][1][2][k];
            quarter1[i * 5 + k].innerHTML = info[i][0][2][k];
            quarterHidden[i * 3 + 2].style.color = "#00ffbc";
        };
    } else {
        name1[i].style.color = "#00ffbc";
        score1[i].style.color = "#00ffbc";
        teamName1[i].style.color = "#00ffbc";
        name2[i].style.color = "#00ffbc";
        score2[i].style.color = "#00ffbc";
        teamName2[i].style.color = "#00ffbc";
        for (let k = 0; k < value; k++){
            quarter1[i * 5 + k].style.color = "#00ffbc";
            quarter2[i * 5 + k].style.color = "#00ffbc";
            quarter1[i * 5 + k].innerHTML = info[i][0][2][k];
            quarter2[i * 5 + k].innerHTML = info[i][1][2][k];
            quarterHidden[i * 3 + 1].style.color = "#00ffbc";
            quarterHidden[i * 3 + 2].style.color = "#00ffbc";
        };
    };
};