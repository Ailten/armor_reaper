
function lerp(a, b, i) {
    return a * (1-i) + b * i;
}

function getBaseUrl() {
    return document.getElementById('base-url').getAttribute('href');
}