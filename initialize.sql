DROP DATABASE IF EXISTS instagram;

CREATE database instagram;
\connect instagram

\i create.SQL

\copy Users(handle)               FROM 'User.csv'     csv header
\copy Personal(uid)               FROM 'Personal.csv'     csv header
\copy Business(uid, category)               FROM 'Business.csv'     csv header
\copy Content_Creator(uid, category)               FROM 'Content_Creator.csv'     csv header
\copy Followers(uid_1, uid_2)               FROM 'Followers.csv'     csv header
\copy Partners_With(cc_uid, b_uid, start_date, end_date, partnership_cost)             FROM 'Partners_With.csv'     csv header
\copy Messages(posted_to, posted_by, message_text, time_sent)               FROM 'Messages.csv'     csv header
\copy Posts(type, caption, uid)               FROM 'Posts.csv'     csv header
\copy Product(name, description, product_price)               FROM 'Product.csv'     csv header
\copy Advertisement(ad_cost, start_date, end_date, product_id, b_uid)               FROM 'Advertisement.csv'     csv header
\copy Likes(post_id, liked_by)               FROM 'Like.csv'     csv header
\copy Comment(post_id, commented_by, comment_text)               FROM 'Comment.csv'     csv header
\copy Promotion(promotion_cost, start_date, end_date, post_id)               FROM 'Promotion.csv'     csv header