"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_index, total_words = 0, len(words)

        while current_index < total_words:
            current_line = []
            current_line.append(words[current_index])
            width = len(words[current_index])
            current_index += 1

            while current_index < total_words and width + 1 + len(words[current_index]) <= maxWidth:
                width += 1 + len(words[current_index])
                current_line.append(words[current_index])
                current_index += 1
            
            if current_index == total_words or len(current_line) == 1:
                current_line = ' '.join(current_line)
                right_extra_spaces = ' ' * (maxWidth - len(current_line))
                result.append(current_line + right_extra_spaces)
                continue
            
            total_spaces = maxWidth - (width - len(current_line) + 1) 
            space_width, extra_spaces = divmod(total_spaces, len(current_line)-1)

            constructed_line = []
            for index, word in enumerate(current_line[:-1]):
                constructed_line.append(word)
                constructed_line.append(" " * (space_width + (1 if index < extra_spaces else 0)))
            constructed_line.append(current_line[-1])
            result.append("".join(constructed_line))
        return result