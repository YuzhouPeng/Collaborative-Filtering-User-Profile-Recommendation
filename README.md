# Collaborative-Filtering-User-Profile-Recommendation

# Design and Methodology of the Collaborative Filtering Approach

![Collaborative Filtering System Design](https://github.com/YuzhouPeng/images/blob/master/Screen%20Shot%202019-02-28%20at%2012.54.20.png)
The design of collaborative filtering is shown in figure. We will introduce main components in the collaborative filtering approach:
Data preprocessing: In the data preprocessing part we will discuss what attributes will be suitable for collaborative filtering approaches.
Forming matrix for learning algorithm: Process of forming user rating matrix will be presented and we will illustrate how we form the rating value for collaborative learning algorithm.


# Data preprocessing for Collaborative Filtering Recom- mendation
For the collaborative filtering approach, we usually need to form a matrix based on our goal for the recommendation. For example, for a recommendation in e-commerce, we usually need to form user-item matrix to find similarity between customers. For a similar book recommendation, we usually need to build item-item matrix to show the inner connection between books.
Thus in our collaborative filtering approach, we decided to form the matrix of user- workexperience-rating matrix (i.e. user as row of matrix, work experience attribute except the first work experience as columns of matrix and value in cells is the rating of work experience, which will be discussed thoroughly in the feature representation section) for collaborative filtering learning algorithms. The reason why we implement the strategy is that the collaborative filtering approach could fit our research aim (i.e. suitable approach for candidate recommendation for jobs). Thus we consider using work experience in the collaborative filtering approach. In order to build data for supervised learning, the job title of first work experience will be the output of learning and user-workexperience-rating matrix will be the output.


# Building Matrix for Collaborative Filtering Approach
We will build a user-workexperience-rating matrix based on the user profile data. The work experience (Columns of matrix) is six work experiences of a user mentioned in section 3.3 and we calculate the rating based on the following rules: For a specific given
32
job title (i.e. software engineer), we will calculate the rating based on following rules: 1. If the job title in the work experience is same as the given job title and the work
year is more or equal than 3 years, the rating value is 2.
2. If the job title in the work experience is the given job title and the work year is
less than 3 years, the rating value is 1.
3. If the job title in the work experience is not the given job title, the rating value
is -1.

![Build matrix of collaborative filtering](https://github.com/YuzhouPeng/images/blob/master/Screen%20Shot%202019-02-28%20at%2013.00.30.png)
