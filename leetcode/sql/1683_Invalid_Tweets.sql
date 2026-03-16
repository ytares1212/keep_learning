-- Table: Tweets
-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | tweet_id       | int     |
-- | content        | varchar |
-- +----------------+---------+
-- tweet_id is the primary key (column with unique values) for this table.
-- content consists of alphanumeric characters, '!', or ' ' and no other special characters.
-- This table contains all the tweets in a social media app.
 
-- Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
-- Return the result table in any order.
-- The result format is in the following example.

-- Example 1:
-- Input: 
-- Tweets table:
-- +----------+-----------------------------------+
-- | tweet_id | content                           |
-- +----------+-----------------------------------+
-- | 1        | Let us Code                       |
-- | 2        | More than fifteen chars are here! |
-- +----------+-----------------------------------+
-- Output: 
-- +----------+
-- | tweet_id |
-- +----------+
-- | 2        |
-- +----------+
-- Explanation: 
-- Tweet 1 has length = 11. It is a valid tweet.
-- Tweet 2 has length = 33. It is an invalid tweet.

-- Solution:
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;

-- why here we use LENGTH instead of CHAR_LENGTH?
-- In this context, LENGTH is used to determine the number of bytes in the content of the tweet. 
-- Since the content consists of alphanumeric characters, '!', or ' ', each character is typically
-- represented by a single byte in most character encodings (like UTF-8). Therefore, LENGTH will give the correct count of characters for this specific case.
-- CHAR_LENGTH, on the other hand, counts the number of characters regardless of how many bytes they take up.
-- In this scenario, since we are only dealing with simple characters that are likely to be single-byte, LENGTH is sufficient and more efficient for our needs.
