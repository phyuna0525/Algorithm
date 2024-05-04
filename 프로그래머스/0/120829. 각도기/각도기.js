function solution(angle) {
    var answer = 0;
    switch (true) {
        case angle > 0 && angle < 90:
            answer = 1;
            break;
        case angle === 90:
            answer = 2;
            break;
        case angle > 90 && angle < 180:
            answer = 3;
            break;
        case angle === 180:
            answer = 4;
            break;
        default:
            answer = 0; 
            break;
    }
    return answer;
}
