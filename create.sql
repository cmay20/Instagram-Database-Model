-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-12-06 05:13:36.956

-- tables
-- Table: Advertisement
CREATE TABLE Advertisement (
    ad_id serial  NOT NULL,
    ad_cost int  NOT NULL,
    start_date date  NOT NULL,
    end_date date  NOT NULL,
    product_id int  NOT NULL,
    b_uid int  NOT NULL,
    CONSTRAINT Advertisement_pk PRIMARY KEY (ad_id)
);

-- Table: Business
CREATE TABLE Business (
    uid int  NOT NULL,
    category text  NOT NULL,
    CONSTRAINT Business_pk PRIMARY KEY (uid)
);

-- Table: Comment
CREATE TABLE Comment (
    post_id int  NOT NULL,
    commented_by int  NOT NULL,
    comment_text text  NOT NULL,
    CONSTRAINT Comment_pk PRIMARY KEY (post_id,commented_by)
);

-- Table: Content_Creator
CREATE TABLE Content_Creator (
    uid int  NOT NULL,
    category text  NOT NULL,
    CONSTRAINT Content_Creator_pk PRIMARY KEY (uid)
);

-- Table: Followers
CREATE TABLE Followers (
    uid_1 int  NOT NULL,
    uid_2 int  NOT NULL,
    CONSTRAINT Followers_pk PRIMARY KEY (uid_1,uid_2)
);

-- Table: Likes
CREATE TABLE Likes (
    post_id int  NOT NULL,
    liked_by int  NOT NULL,
    CONSTRAINT Likes_pk PRIMARY KEY (post_id,liked_by)
);

-- Table: Messages
CREATE TABLE Messages (
    mid serial  NOT NULL,
    posted_to int  NOT NULL,
    posted_by int  NOT NULL,
    message_text text  NOT NULL,
    time_sent timestamp  NOT NULL,
    CONSTRAINT Messages_pk PRIMARY KEY (mid)
);

-- Table: Partners_With
CREATE TABLE Partners_With (
    pid serial  NOT NULL,
    cc_uid int  NOT NULL,
    b_uid int  NOT NULL,
    start_date date  NOT NULL,
    end_date date  NOT NULL,
    partnership_cost int  NOT NULL,
    CONSTRAINT Partners_With_pk PRIMARY KEY (pid)
);

-- Table: Personal
CREATE TABLE Personal (
    uid int  NOT NULL,
    CONSTRAINT Personal_pk PRIMARY KEY (uid)
);

-- Table: Posts
CREATE TABLE Posts (
    post_id serial  NOT NULL,
    type text  NOT NULL,
    caption text  NOT NULL,
    uid int  NOT NULL,
    CONSTRAINT Posts_pk PRIMARY KEY (post_id)
);

-- Table: Product
CREATE TABLE Product (
    product_id serial  NOT NULL,
    name text  NOT NULL,
    description text  NOT NULL,
    product_price int  NOT NULL,
    CONSTRAINT Product_pk PRIMARY KEY (product_id)
);

-- Table: Promotion
CREATE TABLE Promotion (
    promotion_id serial  NOT NULL,
    promotion_cost money  NOT NULL,
    start_date date  NOT NULL,
    end_date date  NOT NULL,
    post_id int  NOT NULL,
    CONSTRAINT Promotion_pk PRIMARY KEY (promotion_id)
);

-- Table: Users
CREATE TABLE Users (
    uid serial  NOT NULL,
    handle text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (uid)
);

-- foreign keys
-- Reference: Advertisement_Business (table: Advertisement)
ALTER TABLE Advertisement ADD CONSTRAINT Advertisement_Business
    FOREIGN KEY (b_uid)
    REFERENCES Business (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Advertisement_Product (table: Advertisement)
ALTER TABLE Advertisement ADD CONSTRAINT Advertisement_Product
    FOREIGN KEY (product_id)
    REFERENCES Product (product_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Business_Partners_With (table: Partners_With)
ALTER TABLE Partners_With ADD CONSTRAINT Business_Partners_With
    FOREIGN KEY (b_uid)
    REFERENCES Business (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Business_User (table: Business)
ALTER TABLE Business ADD CONSTRAINT Business_User
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comment_Posts (table: Comment)
ALTER TABLE Comment ADD CONSTRAINT Comment_Posts
    FOREIGN KEY (post_id)
    REFERENCES Posts (post_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Content_Creator_User (table: Content_Creator)
ALTER TABLE Content_Creator ADD CONSTRAINT Content_Creator_User
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Follower_User (table: Followers)
ALTER TABLE Followers ADD CONSTRAINT Follower_User
    FOREIGN KEY (uid_1)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Follower_User1 (table: Followers)
ALTER TABLE Followers ADD CONSTRAINT Follower_User1
    FOREIGN KEY (uid_2)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Like_Posts (table: Likes)
ALTER TABLE Likes ADD CONSTRAINT Like_Posts
    FOREIGN KEY (post_id)
    REFERENCES Posts (post_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Messages_User (table: Messages)
ALTER TABLE Messages ADD CONSTRAINT Messages_User
    FOREIGN KEY (posted_by)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Partners_With_Content_Creator (table: Partners_With)
ALTER TABLE Partners_With ADD CONSTRAINT Partners_With_Content_Creator
    FOREIGN KEY (cc_uid)
    REFERENCES Content_Creator (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Posts_User (table: Posts)
ALTER TABLE Posts ADD CONSTRAINT Posts_User
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Promotion_Posts (table: Promotion)
ALTER TABLE Promotion ADD CONSTRAINT Promotion_Posts
    FOREIGN KEY (post_id)
    REFERENCES Posts (post_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Comment (table: Comment)
ALTER TABLE Comment ADD CONSTRAINT User_Comment
    FOREIGN KEY (commented_by)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Like (table: Likes)
ALTER TABLE Likes ADD CONSTRAINT User_Like
    FOREIGN KEY (liked_by)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Messages1 (table: Messages)
ALTER TABLE Messages ADD CONSTRAINT User_Messages1
    FOREIGN KEY (posted_to)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Personal (table: Personal)
ALTER TABLE Personal ADD CONSTRAINT User_Personal
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

