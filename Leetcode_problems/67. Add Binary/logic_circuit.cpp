class Solution {
public:
    string addBinary(string a, string b) {
        // ---- from logic circuit point of view ----
        // a basic half adder:
        //   sum = a XOR b
        //   carry a AND b
        //
        // a complete adder:
        //   sum = a XOR b xor carry
        //   carry = (a AND b) + (b AND carry) + (carry AND a)

        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        
        bool digitA = false;
        bool digitB = false;
        bool sum = false;
        bool carry = false;
        string res = "";

        for (int i = 0; i < max(a.length(), b.length()); i++ ){
            digitA = (i < a.length()) ? (a[i] - '0') : false;
            digitB = (i < b.length()) ? (b[i] - '0') : false;

            sum = digitA ^ digitB ^ carry;
            res += (sum + '0');

            carry = (digitA & digitB) | ((digitA ^ digitB) & carry);
        }
        if (carry){
            res += '1';
        }

        reverse(res.begin(), res.end());

        return res;
    }
};