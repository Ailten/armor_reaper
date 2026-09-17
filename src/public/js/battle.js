
window.addEventListener('load', async () => {

    // TODO: place adventurer and mobs in dom.

    for(let i=0; i<battleLog.length; i++){
        await battleLogAnime(battleLog[i]);
        await sleep(1.6);
    }

    // TODO. end of fight print (loose screen, or loot and gains).

});

// ------>

let indexBattleLog
async function battleLogAnime(battleLog){

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
    await playAnimeLog(battleLog);

}

// ------>

function sleep(secondes) {
    return new Promise(resolve => setTimeout(()=>{resolve(null)}, secondes*1000));
}

// ------>

async function playAnimeLog(battleLog) {

    let mainCharacter = getMainCharacterFromLog(battleLog);

    // use a spell.
    if(/^[^ ]+ use [^ ]+ \!$/.test(battleLog)){

        // TODO: make mainCharacter move.

    }
    // affect stats (hp,mp,sp).
    else if(/^[^ ]+ \: (+|\-)[0-9]+ (H|M|S)P$/.test(battleLog)){

        // TODO: make mainCharacter lose stats (over head).

    }
    // die.
    else if(/^[^ ]+ die.$/.test(battleLog)){

        // TODO: make mainCharacter fade out.

    }

}

function getMainCharacterFromLog(battleLog){
    return battleLog.match(/^[^ ]+/);
}