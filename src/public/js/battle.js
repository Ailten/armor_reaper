
window.addEventListener('load', async () => {

    // place adventurer and mobs in dom.
    createCharacterDom(leftTeam, true);
    createCharacterDom(rightTeam, false);

    for(let i=0; i<battleLog.length; i++){
        await battleLogAnime(battleLog[i][0], battleLog[i][1]);
        await sleep(1.6);
    }

    // TODO. end of fight print (loose screen, or loot and gains).

});

// ------>

let indexBattleLog
async function battleLogAnime(battleLog, mainCharacterId){

    let battleLogDom = document.getElementById('battle-log');

    // insert new p.
    let logPDom = battleLogDom.appendChild(document.createElement('p'));
    logPDom.classList.add('battle-log-p');
    logPDom.innerText = battleLog;

    // check if log is overlow (and reduce it).
    while(battleLogDom.scrollHeight > battleLogDom.clientHeight){
        oldestLog = battleLogDom.querySelector('.battle-log-p:first-child')
        if(oldestLog == null){  // theroically never use.
            break;
        }
        battleLogDom.removeChild(oldestLog);
    }

    // play anime.
    await playAnimeLog(battleLog, mainCharacterId);

}

// ------>

function sleep(secondes) {
    return new Promise(resolve => setTimeout(()=>{resolve(null)}, secondes*1000));
}

// ------>

function isUseSpellLog(log){
    return /^[^ ]+ use [^ ]+ \!$/.test(log);
}
function isAffectStatsLog(log){
    return /^[^ ]+ \: (\+|\-)[0-9]+ (H|M|S)P$/.test(log);
}
function isDieLog(log){
    return /^[^ ]+ die.$/.test(log);
}


async function playAnimeLog(battleLog, mainCharacterId) {

    // use a spell.
    if(isUseSpellLog(battleLog)){

        // TODO: make mainCharacter move.

        return;
    }

    // affect stats (hp,mp,sp).
    if(isAffectStatsLog(battleLog)){

        // TODO: make mainCharacter lose stats (over head).

        return;
    }

    // die.
    if(isDieLog(battleLog)){

        // TODO: make mainCharacter fade out.

        return;
    }

}

// ------>

function createCharacterDom(team, isLeft=true){

    let battleScreen = document.getElementById('battle-sreen');
    let baseUrl = getBaseUrl();

    let poss = (isLeft? [
        {x: 30, y: 220},  // left team pos.
        {x: 150, y: 100}
    ]:[
        {x: 430, y: 100},  // right team pos.
        {x: 550, y: 220}
    ]);

    for(let i=0; i<team.length; i++){
        characterData = team[i];

        let div = battleScreen.appendChild(document.createElement('div'));
        div.classList.add('battle-character-dom');
        div.setAttribute('character-id', characterData.id)
        div.style.backgroundImage = `url("${baseUrl}public/img/characters/${characterData.skin}.png")`;

        // symetry horizontaly (for right team).
        if(!isLeft){
            div.style.transform = 'scaleX(-1)';
        }

        // set pos.
        if(team.length == 1){
            div.style.left = `${lerp(poss[0].x, poss[1].x, 0.5)}px`;
            div.style.top = `${lerp(poss[0].y, poss[1].y, 0.5)}px`;
        }else{
            let interpolate = i / (team.length - 1)
            div.style.left = `${lerp(poss[0].x, poss[1].x, interpolate)}px`;
            div.style.top = `${lerp(poss[0].y, poss[1].y, interpolate)}px`;
        }

        // z-index.
        div.style.zIndex = (isLeft?
            team.length-1-i:
            i
        )*10 + 10;

    }

}
