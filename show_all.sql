\connect instagram;

\echo (The Users table stores all information about users, including their id and handle)
SELECT* FROM Users;

\echo (Personal users are Users)
SELECT* FROM Personal;

\echo (Businesses are Users, except they also have a category)
SELECT* FROM Business;

\echo (Content_Creators are also users, except they also have a category)
SELECT* FROM Content_Creator;

\echo (The Comment Table stores all information about post comments, including who wrote the comment, the post thats being commented on, and the comment_text)
SELECT* FROM Comment;

\echo (The Followers table stores all the followers information, including the follower, and the person who is being followed)
SELECT* FROM Followers;

\echo (The Likes table stores all the post likes information, including who liked the post and the post thats being liked)
SELECT* FROM Likes;

\echo (The Messages table stores all the messages information, including posted to, posted by, the message text , and the time sent)
SELECT* FROM Messages;

\echo (The Partners_With table stores all the information about partnerships, including the start date, end date, cost, and the creator and business who are partnered)
SELECT* FROM Partners_With;

\echo (The Advertisement table stores all information about advertisements, including cost, start_date, and end_date)
SELECT* FROM Advertisement;

\echo (The Posts table stores all information about posts, including post type, caption, and the person that made the post)
SELECT* FROM Posts;

\echo (The Product table stores all information about products that are advertised, including the name, description, and price)
SELECT* FROM Product;

\echo (The Promotion table stores all information about post promotions, including their cost, start date, end date, and the post that is being promoted)
SELECT* FROM Promotion;

