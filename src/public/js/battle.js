
window.addEventListener('load', async () => {

    // place adventurer and mobs in dom.
    createCharacterDom(leftTeam, true);
    createCharacterDom(rightTeam, false);

    for(let i=0; i<battleLog.length; i++){
        await battleLogAnime(battleLog[i][0], battleLog[i][1]);
        if(battleLog[i][0].startsWith('<mask>'))
            continue;
        await sleep(0.3);
    }

    // TODO. end of fight print (loose screen, or loot and gains).

});

// ------>

let indexBattleLog
async function battleLogAnime(battleLog, mainCharacterId){
    let isMaskedLog = battleLog.startsWith('<mask>');
    if (isMaskedLog){
        // skip print log.
        await playAnimeLog(battleLog, mainCharacterId);
        return;
    }
    
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
    let isMaskedLog = battleLog.startsWith('<mask>');
    if (isMaskedLog){
        battleLog.replace('<mask>', '');
    }

    //if(mainCharacterId == -1)
    //    return;

    let mainCharDom = document.querySelector(`div[character-id="${mainCharacterId}"].battle-character-dom`);

    // use a spell.
    if(isUseSpellLog(battleLog)){

        if(mainCharDom.hasAttribute('character-is-left')){
            mainCharDom.classList.add('character-move-left');
        }else{
            mainCharDom.classList.add('character-move-right');
        }

        await sleep(1);

        if(mainCharDom.classList.contains('character-move-left')){
            mainCharDom.classList.remove('character-move-left');
        }
        if(mainCharDom.classList.contains('character-move-right')){
            mainCharDom.classList.remove('character-move-right');
        }

        return;
    }

    // affect stats (hp,mp,sp).
    if(isAffectStatsLog(battleLog)){

        let battleScreenDom = document.getElementById('battle-sreen');
        let statsTxtDom = null;
    
        // get str.
        let strStatsEdit = battleLog.match(/[\+\-][0-9]+ [HMS]P$/)[0];

        if (!isMaskedLog){
    
            // build a dom stats message.
            statsTxtDom = battleScreenDom.appendChild(document.createElement('div'));
            statsTxtDom.classList.add('stats-edit-fx');
            statsTxtDom.classList.add(
                strStatsEdit.endsWith('HP') ? 'stats-edit-hp':
                strStatsEdit.endsWith('MP') ? 'stats-edit-mp':
                'stats-edit-sp');
            statsTxtDom.style.zIndex = '200';
            statsTxtDom.innerText = strStatsEdit;
    
            // set pos.
            let posX = mainCharDom.offsetLeft + (mainCharDom.offsetWidth - statsTxtDom.offsetWidth) * 0.5;
            statsTxtDom.style.left = `${posX}px`;
            let posY = mainCharDom.offsetTop - statsTxtDom.offsetHeight;
            statsTxtDom.style.top = `${posY}px`;
    
        }

        // reducing stats jauge.
        let jaugeDom = mainCharDom.querySelector(
            strStatsEdit.endsWith('HP') ? '.hp-jauge':
            strStatsEdit.endsWith('MP') ? '.mp-jauge':
            '.sp-jauge'
        );
        if(jaugeDom != null){
            let jaugeValue = Number(jaugeDom.getAttribute('value'));
            let jaugeValueMax = Number(jaugeDom.getAttribute('max'));
            let amountEdit = Number(strStatsEdit.match(/[0-9]+/)[0]);
            if(strStatsEdit.includes('-')){
                amountEdit *= -1;
            }
            jaugeValue += amountEdit
            jaugeValue = Math.min(Math.max(jaugeValue, 0), jaugeValueMax);
            let interpolateJauveValue = jaugeValue / jaugeValueMax;
            let purcentJaugeValue = Math.ceil(interpolateJauveValue * 100);
            jaugeDom.getElementsByTagName('div')[0].style.width = `${purcentJaugeValue}%`;
            jaugeDom.setAttribute('value', jaugeValue);
        }

        if (isMaskedLog)
            return
        
        await sleep(1);

        // delete the fx message.
        battleScreenDom.removeChild(statsTxtDom);

        return;
    }

    // die.
    if(isDieLog(battleLog)){

        mainCharDom.classList.add('character-die');

        await sleep(1);

        mainCharDom.parentNode.removeChild(mainCharDom);

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
        div.setAttribute('character-id', characterData.id);
        if(isLeft){
            div.setAttribute('character-is-left', 'true');
        }
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

        // add jauge stats:
        let hpJauge = div.appendChild(document.createElement('div'));  // hp.
        hpJauge.classList.add('stats-jauge', 'hp-jauge');
        hpJauge.setAttribute('max', characterData.hp);
        hpJauge.setAttribute('value', characterData.hp);
        hpJauge.appendChild(document.createElement('div'));
        let mpJauge = div.appendChild(document.createElement('div'));  // mp.
        mpJauge.classList.add('stats-jauge', 'mp-jauge');
        mpJauge.setAttribute('max', characterData.mp);
        mpJauge.setAttribute('value', characterData.mp);
        mpJauge.appendChild(document.createElement('div'));
        let spJauge = div.appendChild(document.createElement('div'));  // sp.
        spJauge.classList.add('stats-jauge', 'sp-jauge');
        spJauge.setAttribute('max', characterData.sp);
        spJauge.setAttribute('value', characterData.sp);
        spJauge.appendChild(document.createElement('div'));

    }

}
