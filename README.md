# Table of contents
* [Purpose](#purpose)
* [User Experience](#user-experience)
  * [User Stories](#user-stories) 
  * [Design](#design)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Features Left To Implement](#features-left-to-implement)
* [Technologies](#technologies)
* [Testing](#testing)
  * [Validator Testing](#validator-testing)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)

# Milestone Project 4 - Gamernetic
## Purpose

This website was created to complete the fourth Milestone Project for Code Insitute's Full Stack Software Developer course. I built this from the ground up using knowledge I gained from the previous modules. The objective of this project is to showcase my ability to create a true Full Stack application using the Django framework. The full list of technologies used can be found in the technologies section further down.

Users of this website are able to create, read, update and delete posts regarding any subject in the gaming industry.

You can find the link to the live website right [here](https://gamernetic.herokuapp.com/).
Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

![image](https://user-images.githubusercontent.com/98277650/188247357-c4c72544-90cd-4264-844c-f7e88695a8ab.png)

***

# User Experience
## User Stories
### First Time User Goals
<details><summary>First Time User Goals</summary>

* As a First Time User, I clearly understand the main objective of the website.
* As a First Time User, I can easily navigate through the website.
* As a First Time User, I can register an account to gain full access to the website.
* As a First Time User, I can view more from the creator of the website via their social media accounts.
* As a First Time User, I can choose a post I would like to inspect further.
</details>
<details><summary>Frequent User Goals</summary>

* As a Frequent User, I can log in to gain access to my account.
* As a Frequent User, I can create my own blog post and post it on the website.
* As a Frequent User, I can edit or delete my own posts.
* As a Frequent User, I can comment on a blog post with my thoughts on the subject.
* As a Frequent User, I can like a post to show that I enjoyed it.
* As a Frequent User, I can share a post to my own personal social media account.
* As a Frequent User, I can change aspects of my personal account details.
* As a Frequent User, I can change my password incase their is a security risk.
</details>

<details><summary>Admin User Goals</summary>

* As an Admin, I can create, read, update and delete posts so that I can manage my blog content.
* As an Admin, I can create draft posts so that I can finish writing the content later.
* As an Admin, I can approve or disapprove comments so that I can filter out objectionable comments.
</details>

***
## Design

<details>
<summary>Wireframes</summary>

* Home Page Desktop:

![index-desktop-wireframe](static/images/readme/wireframes/index-desktop-wireframe.png)

* Home Page Mobile:

![index-mobile-wireframe](static/images/readme/wireframes/index-mobile-wireframe.png)

* Post Content:

![post-content-wireframe](static/images/readme/wireframes/post-content.png)

* Add Post:

![add-post-wireframe](static/images/readme/wireframes/add-post.png)

* Log In:

![log-in-wireframe](static/images/readme/wireframes/log-in.png)

</details>

<details><summary>Imagery</summary>
The images you are greeted to when entering the website are of varying style. Most of the photos you will see are uploaded by the user, but the header image will always be as shown below. This is also used as the placeholder image when a user chooses to not upload a photo to their post.

![Imagery](static/images/readme/readme-placeholder.jpg)
</details>

<details><summary>Color Scheme</summary>
Three colors are used in this website, these being #000000, #FFFFFF and #FF0030. The background, text and foreground colors have a sufficient contrast ratio to aid with accessibility.

![Color Pallete](static/images/readme/palette.png)
</details>

<details><summary>Fonts</summary>
The font used throughout the website is Space Grotesk. I used only 1 font for the site, but used text-transform to make some of the text uppercase.

![Fonts](static/images/readme/readme-font.png)
</details>

***

# Features
## Existing Features
<details><summary>Home Page</summary>
 
The first thing users are greeted to is the Home Page. This is where you will find everything to navigate the website.

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I clearly understand the main objective of the website.
```
![image](https://user-images.githubusercontent.com/98277650/188748847-5563753e-e0d7-4d44-a1b1-7996547ff706.png)
 
</details>

<details><summary>Navigation Bar</summary>
 
Featured at the top of all pages is the nav bar, holding the Gamernetic logo and all links to the home page, register page and log in page.

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can easily navigate through the website.
```
![image](https://user-images.githubusercontent.com/98277650/188245525-36fe6adc-d3e7-45dc-80f7-5130991190b2.png)

I have also set up the Nav Bar to be viewed on smaller screen sizes, with the help of Bootstraps .navbar-toggler class.

![image](https://user-images.githubusercontent.com/98277650/188749607-8643846a-77b6-4970-bdb8-edab95b1e5f2.png)

</details> 

<details><summary>Footer</summary>
 
Featured at the bottom of all pages is the footer, holding all links to my personal social media accounts.

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can view more from the creator of the website via their social media accounts.
```
![image](https://user-images.githubusercontent.com/98277650/188749256-c830d891-527d-4d64-ab4f-2c2d7c1ab900.png)
 
</details>

<details><summary>Post Detail</summary>
 
When one of the posts on the home page is clicked, the user is taken to post detail view. Here the user can see the author, date/time posted and the content itself.



The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can choose a post I would like to inspect further.
```
![image](https://user-images.githubusercontent.com/98277650/188749721-9345eef1-0846-4a4d-b8be-72f458072e50.png)
 
</details>

<details><summary>Like/Unlike</summary>
 
Just below the post itself, two icons are visible. One of these being a clickable Like button that can only be interacted with when the user has logged in. The second icon shows the amount of comments the post has recieved.

The purpose of this is to fulfill the following user story:
```
As a Frequent User, I can like a post to show that I enjoyed it.
```
![image](static/images/readme/like-unlike.png)

I also added a link that will enable the user to share the blog post to their own Twitter account.

The purpose of this is to fulfill the following user story:
```
As a Frequent User, I can share a post to my own personal social media account.
```
![image](static/images/readme/twitter-share.png)

</details>

<details><summary>Post Comments</summary>
 
At the bottom of the post is the comments section, where the user is able to write and post a comment on the blog post.

The purpose of this is to fulfill the following user story:
```
As a Frequent User, I can comment on a blog post with my thoughts on the subject.
```
![image](https://user-images.githubusercontent.com/98277650/188749804-bde80368-9193-471d-8a64-3e419e1adebe.png)

When the user has posted a comment, an alert replaces the text field letting them know that their comment is awaiting inspection and approval.

The purpose of this is to fulfill the following user story:
```
As an Admin, I can approve or disapprove comments so that I can filter out objectionable comments.
```

![image](https://user-images.githubusercontent.com/98277650/188749923-dfdab3c8-331c-47c1-99a0-e4f917a0f4af.png)
 
</details>

<details><summary>Add Post</summary>
 
This page of the website allows the user to create their own blog post. I implemented a rich text editor which allows the user to add a bit more style to their post. For security reasons I have to give the user staff privileges to be able to post, which is common practice in other professional websites. This is to ensure that not just anyone off the internet can find my website and post questionable things.

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can create my own blog post and post it on the website.
```
![image](https://user-images.githubusercontent.com/98277650/188750032-7fd19423-9acf-4851-80fb-bb2af0e0365b.png)

</details>

<details><summary>Edit/Delete Post</summary>
 
If the user is the author of the post, two buttons appear on the post detail section giving them the ability to edit or delete the post. This is to aid the user in correcting issues with the post, or just to delete it and start again fresh.

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can edit or delete my own posts.
```
![image](https://user-images.githubusercontent.com/98277650/188750267-9fe41ace-f585-42a9-bafa-7c69fdb28e04.png)

![image](https://user-images.githubusercontent.com/98277650/188750296-f19bc082-072f-4a46-8a2a-2f2c240afc16.png)

When the user clicks the delete button they are taken to a new page with a warning, making sure they are aware that they are about to permanently delete the post. This is so if they change their mind and want to keep it, they can.

![image](https://user-images.githubusercontent.com/98277650/188750325-c4fde938-07be-45cd-b2bd-5104da48feb0.png)

</details>

<details><summary>Register</summary>
 
If the visitor likes the website, they are able to register an account. This enables the user to be able to like and comment on posts.

The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can register an account to gain full access to the website.
```
![image](static/images/readme/register.png)

</details>

<details><summary>Log In</summary>
 
When the user returns to the website to see if any more blog posts have been created, they are able to log back in.

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can log in to gain access to my account.
```
![image](static/images/readme/login.png)

</details>

<details><summary>Edit Profile</summary>
 
This page of the website enables the user to edit specific things regarding their account. These being:
* Username
* Email
* First Name
* Last Name

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can change aspects of my personal account details.
```
![image](https://user-images.githubusercontent.com/98277650/188750457-33d23728-d41b-4f35-b28f-2f82f222a4ee.png)

</details>

<details><summary>Change Password</summary>
 
Within the Edit Profile page the user also has the option to click a link to take them to a page allowing them to change their password. 

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can change my password incase their is a security risk.
```
![image](https://user-images.githubusercontent.com/98277650/188750520-6c1ae6aa-0d5e-40cf-8503-e93681af33c1.png)

When the user has confirmed their new password, they are taken to a page informing them that the change was successful.

![image](https://user-images.githubusercontent.com/98277650/188750658-7ab3a60d-910c-48ab-b3bd-b952d783273c.png)

</details>

## Features Left to Implement

<details><summary>Password Reset</summary>
I would like to implement a password reset feature. This would send an email to the users associated email address with a temporary password. They would then use said password to gain access to their account and change their password manually.
</details>

<details><summary>Contact Us</summary>
I would like to eventually implement a Contact Us page to the website. Users would be able to send enquiries to me via a form.
</details>

<details><summary>Reply to comments</summary>
I would like to add a feature that allows the user to reply to comments on a post. This could be a reply in a thread format or something else entirely. This would add a personal touch to the comments section, enabling users to interact with one another.
</details>

***

# Technologies

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
* [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
* [Heroku](https://dashboard.heroku.com/)
    * Heroku is the site used to deploy the project.
* [GitHub](https://github.com/)
    * GitHub is the hosting site I used to store the code for the website.
* [GitPod](https://gitpod.io/)
    * GitPod is the Integrated Development Environment used to develop the website in a browser.
* [Font Awesome](https://fontawesome.com/)
    * Font Awesome icons are used for the social media links located in the Footer section of the website.
* [Google Fonts](https://fonts.google.com/)
    * Google fonts are used in the project to import the **Space Grotesk** font.
* [Quicktools by Picsart](https://tools.picsart.com/)
    * Quicktools by Picsart is used to generate the image of the color pallete.
* [Am I Responsive?](http://ami.responsivedesign.is/)
    * Am I Responsive is used to generate the website mock up.
* [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
    * The built in developer tools in Google Chrome are used to test CSS styles, inspect page elements and help with debugging problems with the layout of the website.
* [Stack Overflow](https://stackoverflow.com/)
    * Stack Overflow was the primary source for help regarding issues.
* [W3 Schools](https://www.w3schools.com/)
    * W3 Schools was one of the websites used for resolving issues with code.

***

# Testing

## Validator Testing

### Code Validation

To ensure all code for Gamernetic was correct, validation through various validators was performed. The results are listed below.

* HTML Validation

  All HTML code was checked with the [W3C Markup Validation Service](https://validator.w3.org/).

   <details>
   <summary>Home Page</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187966508-55661019-a2bf-4dd3-854a-0ccdb0f3deb5.png)

   </details>
   <details>
   <summary>Post Detail</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187970183-669819b5-5aa2-4d9c-9f3d-9942281ebacb.png)

   </details>
   <details>
   <summary>Sign Up</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187970451-f03bd49b-3d62-4076-9a40-530f141173f1.png)

   </details>
   <details>
   <summary>Log In</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187970742-d2c2e134-b7e6-42fd-af15-919449424abd.png)

   </details>
   <details>
   <summary>Add Post</summary>

   One error returned. As seen in the code below, I have had to use {{ form.as_p }} to get the rich text editor to function correctly. As of right now I am unsure of a solution.

   ![image](https://user-images.githubusercontent.com/98277650/187972452-e1a36e47-c8ec-4367-9b6a-595ed69114de.png)


   ![image](https://user-images.githubusercontent.com/98277650/187972057-046a277d-71b6-4eac-8f6a-1754f95f633f.png)

   </details>
   <details>
   <summary>Edit Profile</summary>

   I was unable to validate this page due to the page only being accessible to a user who is logged in and able to edit their profile.

   ![image](https://user-images.githubusercontent.com/98277650/187972974-6047d7bb-40ea-4596-9c23-f18c3a808ccc.png)

   </details>
   <details>
   <summary>Log Out</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187973621-a01a08f4-4271-4ef0-826e-7f3eb836001f.png)

   </details>
   
* CSS Validation

  All CSS code was checked with the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

   <details>
   <summary>CSS Results</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187975424-1d87fd98-b930-4009-874a-adbb4210bd86.png)

   </details>
   
* Python Validation

  All Python code was checked with the [PEP8 Online Service](http://pep8online.com/).

  <details>
  <summary>admin.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188003211-31fd93b3-c8bb-4e13-ab52-b9ef5f929f03.png)

  </details>
  <details>
  <summary>apps.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188003527-aa13b4d9-f627-474e-a6d2-8aafae96a2f9.png)

  </details>
  <details>
  <summary>forms.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188004880-1f45b1fa-234b-42d9-9b09-01a9201fb825.png)

  </details>
  <details>
  <summary>models.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188005177-1c8a8ed1-2d8a-4de6-aab0-e5c2b07e8efc.png)

  </details>
  <details>
  <summary>urls.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188005370-ba06262e-cb7e-4d7f-b5a2-443bd9b1282a.png)

  </details>
  <details>
  <summary>views.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188005494-cc4cd2bd-4cd8-446a-a2a2-0681761026f8.png)

  </details>

* Accessibility

  The websites accessibility was tested with the [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/).

  <details>
  <summary>WAVE report</summary>

  ![image](static/images/readme/wave.png)

  </details>

## Manual Testing

  I tested that the website is responsive, functions well and looks good on all screen sizes using Google Dev Tools and Responsive Design Checker.

  <details><summary>Google Doc</summary>

  ![image](static/images/readme/manual-testing.png)

  </details>

***

## Bugs
For this website I decided to open a project on the GitHub repository, that I would add to as I go along. This is to aid with the transparency of my coding, showing the bugs I encountered and how they were fixed.  
* [CKEDITOR causing deployment failure](https://github.com/jrdnbrkfld/pp4-gamernetic/issues/23)
* [Requires the user to create their own slug field.](https://github.com/jrdnbrkfld/pp4-gamernetic/issues/25)

***

# Deployment

 This project was deployed using Code Institute's mock terminal for Heroku.
* Fork or clone this repository
* Create a new Heroku app
* Set the buildpacks to Python and NodeJS in that order
* Link the Heroku app to the repository
* Click on Deploy

***

# Credits
I'd like to thank my mentor [Ronan McClelland](https://www.linkedin.com/in/ronanmcclelland/) for their help and support throughout this project. I'd also like to thank my cohorts in the Code Institute Slack community, and the Tutor Assistance for all their help with code issues.

The [Code Institute Python Template](https://github.com/Code-Institute-Org/python-essentials-template) was used as a base for this project and made into my own.