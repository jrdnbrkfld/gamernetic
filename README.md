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
  * [Issues And Resolutions](#issues-and-resolutions)
* [Deployment](#deployment)
* [Credits](#credits)

# Milestone Project 4 - Gamernetic
## Purpose

This website was created to complete the fourth Milestone Project for Code Insitute's Full Stack Software Developer course. I built this from the ground up using knowledge I gained from the previous modules. The objective of this project is to showcase my ability to create a true Full Stack application using the Django framework. The full list of technologies used can be found in the technologies section further down.

Users of this website are able to create, read, update and delete posts regarding any subject in the gaming industry.

You can find the link to the live website right [here](https://gamernetic.herokuapp.com/).
Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

![image](https://user-images.githubusercontent.com/98277650/187801886-aed9a86e-2f82-4f94-bddc-f9f509b24c6e.png)

## User Experience
### User Stories
#### Site User Goals
* As a Site User I can view a list of posts so that I can select one to read.
* As a Site User I can click on a post so that I can read the full article.
* As a Site User I can view the number of likes on each post so that I can see which is the most popular or viral.
* As a Site User I can view comments on an individual post so that I can read the conversation.
* As a Site User I can register an account so that I can comment on and like posts.
* As a Site User I can leave comments on a post so that I can be involved in the conversation.
* As a Site User I can like or unlike a post so that I can interact with the content.
* As a Site User I can navigate around the site so that I can choose the things I want to read.
* As a Site User I can create my own post to add to the blog.
* As a Site User I can update/edit my own post to add to the blog.
* As a Site User I can edit/delete my own post from the blog.
* As a Site User I can view and edit my profile so that I can customise how I appear on the website..

#### Admin User Goals
* As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.
* As a Site Admin I can create draft posts so that I can finish writing the content later.
* As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.

## Design

<details>
<summary>Wireframes</summary>

![index-desktop-wireframe](https://user-images.githubusercontent.com/98277650/177381328-736c7454-6a29-4ba5-8a5b-94af1189cc14.png)
![index-mobile-wireframe](https://user-images.githubusercontent.com/98277650/177381382-971e05ca-ca33-46c5-9997-61c2210c2a18.png)
</details>

## Features

### Existing Features

### Features Left to Implement

## Technologies

## Testing

## Validator Testing

### Code Validation

To ensure all code for Gamernetic was correct, validation through various validators was performed. The results are listed below.

- ### HTML Validation

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
   
- ### CSS Validation

  All CSS code was checked with the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

   <details>
   <summary>CSS Results</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187975424-1d87fd98-b930-4009-874a-adbb4210bd86.png)

   </details>
   
- ### Python Validation

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

## Issues and Resolutions

## Deployment

## Credits
