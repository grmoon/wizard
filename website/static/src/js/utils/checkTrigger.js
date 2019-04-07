function checkE(triggerValue, answerValue) {
    return triggerValue == answerValue;
}

function checkIN(triggerValue, answerValue) {
    return answerValue !== null && answerValue.indexOf(triggerValue) !== -1;
}

function checkGT(triggerValue, answerValue) {
    return answerValue !== null && triggerValue > answerValue;
}

function checkGTE(triggerValue, answerValue) {
    return answerValue !== null && triggerValue >= answerValue;
}

function checkLT(triggerValue, answerValue) {
    return answerValue !== null && triggerValue < answerValue;
}

function checkLTE(triggerValue, answerValue) {
    return answerValue !== null && triggerValue <= answerValue;
}

export default function(trigger, answer) {
    let func;

    switch(trigger.condition) {
        case 'E':
            func = checkE;
            break;
        case 'IN':
            func = checkIN;
            break;
        case 'GT':
            func = checkGT;
            break;
        case 'GTE':
            func = checkGTE;
            break;
        case 'LT':
            func = checkLT;
            break;
        case 'LTE':
            func = checkLTE;
            break;
        default:
            throw new Error(`${trigger.condition} is not a supported trigger condition.`);
    }

    return func(trigger.value, answer.value);
}