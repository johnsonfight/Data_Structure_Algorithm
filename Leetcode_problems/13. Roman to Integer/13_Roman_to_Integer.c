int romanToInt(char * s){
    int t['X' + 1] = {
        ['I'] = 1,
        ['V'] = 5,
        ['X'] = 10,
        ['L'] = 50,
        ['C'] = 100,
        ['D'] = 500,
        ['M'] = 1000,
    };
    /* A simple hash table implemented with array
        C : t[67] = 100
        D : t[68] = 500
        I : t[73] = 1
        L : t[76] = 50
        M : t[77] = 1000
        V : t[86] = 5
        X : t[88] = 10
    */

    int output = 0;
    for (int i = 0; s[i]; i++) {
        if (t[s[i]] < t[s[i+1]]){
            output -= t[s[i]];
        }
        else{
            output += t[s[i]];
        }
    }
    return output;
}