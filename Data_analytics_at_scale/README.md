**How about you readme?**

# Data Analytics at Scale Summative Assessment

You have been contracted as a consultant for Find Images Now (FIN), a tech start-up that wants to match and cluster images at scale. FIN has identified a promising technique but needs help evaluating the performance of the approach. Your evaluation should assess both the accuracy and computational costs (e.g., CPU, memory, runtime demands and how these scale with the number of images as input). 

In particular, FIN has identified “image hashing” approaches and identified the image hash library in Python: https://github.com/JohannesBuchner/imagehash as well as its own in-house hashing approach, called FINd, for which a pure Python implementation is available at https://github.com/oxfordinternetinstitute/das2020 . 
Candidates must first seek to optimize FINd by identifying what portions of the algorithm are computational bottlenecks, implementing alternatives, and comparing computational performance. Candidates must plan and implement two or three optimizations. These optimizations may include: 
- use of scientific Python library such as numpy, scipy, and pandas, different execution approaches (e.g., single process on one CPU vs multiprocessing on a single computer vs distributed approaches), 
- use of GPUs, 
- use of C-compiled code (i.e., cython), 
- etc.

When implementing the optimizations, candidates should ensure the correctness of their output by writing an appropriate unit test. They should also profile the code to analyse CPU, memory, runtime, and other relevant aspects of computational performance.  

After this, candidates must compare the performance (both in terms of accuracy and computational costs) of two methods from the imagehash library to their optimized version of FINd using the dataset provided in class. That is, compare FINd with any two of the following from the imagehash library: 
- average hashing (aHash) 
- perception hashing (pHash) 
- difference hashing (dHash) 
- wavelet hashing (wHash) 

FIN expect a written report, not to exceed 3,500 words, consisting of two parts. Part 1 will report on FINd including an initial assessment of the performance of the code, the optimizations attempted, and the resulting changes (positive or negative) in computational performance. Candidates should discuss any relevant trade-offs (e.g., CPU vs. memory) of these optimizations. The second half of the report should focus on how FINd compares to the two other image hashing methods selected. This part should analyse both the accuracy of the results as well as the computational costs. The report should focus most in-depth on the trade-offs of different approaches (e.g., the advantages and disadvantages of each approach and how the approaches compare to one another). Finally, candidates should discuss which approach is the 'best' for the given dataset and FIN’s need to match similar images at scale. 
