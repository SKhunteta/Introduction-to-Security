HOW TO RUN
________________________________________
Run

sudo pip install bitarray
sudo pip install mmh3


QUESTIONS
________________________________________

a) What hash functions did you choose and why (Hint: Cryptographic or non-cryptographic)? What is the output range of the hash functions? What is the size of the Bloom filter in each case?

The hash function I used was mmh3. I used mmh3 because it was pretty straightforward and easy to use in Python. Mmh3 is non-cryptographic. Murmurhash is simple, has good distribution and good collision resistance. The size of the bloom filter I calculated to be 8964670. The size of the dictionary (the inserted elements) was 623517.

b) How long does it take for your Bloom Filter to check 1 password in each case? Why does one perform better than other?

I put a time test in my code that checks how long it takes to check the entire bloom filter. For the overall bloom filter with every word, it takes about 0.0008 seconds to check the dictionary with the three hashes, and nearly 0.0014 seconds to check the dictionary with five hashes.

c) What is the probability of False Positive in your Bloom Filter in each case? What is the probability of False Negative in your Bloom Filter? 

You cannot have false negatives in the bloom filter. You can, however, have false positives. The formula for false positives is calculated by (m/n)ln2. Here, m is the number of bits in the array and n is the number of inserted elements. Now, we already figured out the size of the bloom filter was 8964670. We also figured out that the size of the dictionary (the inserted elements) was 623517.

So using the below link, I was able to check the false positive rate of each. 8962670/623517 is about 14. So I checked the error rate that corresponded to that using a k (number of hash functions) of both 3 and 5. So the error rate for a hash function of 3 is .7%, and the error rate for a hash function of 5 was .2%.

http://pages.cs.wisc.edu/~cao/papers/summary-cache/node8.html

d) How can you reduce the rate of False Positives?

Reducing false positives is simple - the rate of false positives decreases as m increases, and increases as n increases. The fewer elements are inserted, the lower the rate of false positives. On that same measure, however, if the size of the bloom filter increases then the rate of false positives decreases.