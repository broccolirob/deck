/**
 * Created by robert on 9/16/14.
 * @return {string}
 */

function FirstReverse (str) {
    return str.split("").reverse().join("");
}

/**
 * @return {number}
 */
function FirstFactorial (num) {
    if (num == 1) {
        return 1;
    }
    return num * FirstFactorial (num-1);
}

function LongestWord(sen) {
  var sentence = sen.split(" ").sort(function(a,b){
    return b.replace(/[^a-zA-Z]/g, "").length - a.replace(/[^a-zA-Z]/g, "").length;
  });
  return sentence.shift();
}

FirstReverse("my string");
FirstFactorial(5);
LongestWord("Which word has the longest string");


