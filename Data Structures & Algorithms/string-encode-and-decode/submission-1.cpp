class Solution {
private:
    char toHexDigit(int value) {
        if (value < 10) {
            return static_cast<char>('0' + value);
        }

        return static_cast<char>('A' + (value - 10));
    }

    int fromHexDigit(char c) {
        if (c >= '0' && c <= '9') {
            return c - '0';
        }

        if (c >= 'A' && c <= 'F') {
            return c - 'A' + 10;
        }

        if (c >= 'a' && c <= 'f') {
            return c - 'a' + 10;
        }

        return -1;
    }

public:
    string encode(vector<string>& strs) {
        string encoded;

        for (const string& str : strs) {
            for (unsigned char character : str) {
                encoded += toHexDigit(character >> 4);

                encoded += toHexDigit(character & 0x0F);
            }

            encoded += ';';
        }

        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> result;
        string currentHex;

        for (char character : s) {
            if (character != ';') {
                currentHex += character;
                continue;
            }

            string decodedString;

            for (int i = 0; i < static_cast<int>(currentHex.size()); i += 2) {
                int high = fromHexDigit(currentHex[i]);
                int low = fromHexDigit(currentHex[i + 1]);

                char originalCharacter =
                    static_cast<char>((high << 4) | low);

                decodedString += originalCharacter;
            }

            result.push_back(decodedString);
            currentHex.clear();
        }

        return result;
    }
};