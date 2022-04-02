# P09_de_bontin
9th project of my studies : building a responsive django web app

## Launching the server
#### Download the repository content from github
- Create a new folder, and name it as you want `mkdir newfolder`    
- Enter your new folder `cd newfolder`    
- Clone the repository `git clone 'https://github.com/likhardcore/P09_de_bontin.git'`    

#### Setup the server
- Enter the project general folder `cd P09_de_bontin`    
- Create a new virtual environment `python -m venv env`    
- Enter the virtuel environment `env/scripts/activate`    
- Install the dependencies `pip install -r requirements.txt`    
- Enter the project folder `cd litreview`    
- Run the server `python manage.py runserver`    

#### Login
- The server is accessible from any browser like Chrome, Firefox, Brave...    
- Enter "http://127.0.0.1:8000/" in the search bar    
- You are now on the login page. Like any other website, you can either create a new profil or login if you already have one.    
- (Here is a list of some profils that already exist : Likha, Muii, Louis, Java, Spoon, Flolasticot, Palme, Jacobr, CosmicChrist. The password is the same for every profils : Jambon12)
- You can explore the database by logging in with a super user. Here are the two superusers that already exist : Chirac, LeZ. The password is also : Jambon12. You can access the superuser environment by typing "http://127.0.0.1:8000/admin/" in the search bar of your browser.
- Once you are logged in, you are redirected on the pubic flux, and some options are available to you. Let's explore them.  


## Using the website
### Differents flux
- The differents types of flux select which tickets and reviews to display.    
- On each ticket, the user can add a review, access the flux of the corresponding ticket, access the flux of the corresponding book, or access the profil of the poster. It displays all the informations conserning the book that the poster gave. If the user is the poster, he can access his profil, or the modifying form to update or delete his ticket.    
- On each review, the user can add his, access the flux of the corresponding book, access the profil of the related ticket's poster, or the profil of the review poster. If the user is the poster, he can access his profil, or the modifying form to update or delete his review. It displays some informations about the book (title, author, cover if any), and the grade and comment writen by the poster.    
- All of the differents flux are paginated with a limit of 5 article per page. The pagination is displayed only if the number of article is above this limit.

###### Public flux
- This page is accessible at "http://127.0.0.1:8000/flux", or by clicking "Flux publique" on the side bar. The user can see all the tickets and reviews posted by the community order by date. The most recent first.
- There also is 2 buttons on the top of the page that allow the user to either ask a review, or give one.

###### Custom flux
- This page is accessible at "http://127.0.0.1:8000/flux/perso/", or by clicking "Flux personnalisé" on the side bar. It displays 3 types of data. First : the posts (tickets and reviews) posted by people the user follows, second, the user's own posts and finaly the reviews that answer to the user's tickets. The program order all this by date.
- There also is 2 buttons on the top of the page that allow the user to either ask a review, or give one.

###### Self flux
- This page is accessible at "http://127.0.0.1:8000/flux/self/", or by clicking "Flux personnalisé" on the side bar. It displays only the post the user wrote. He can also access it by clicking his pseudo in the side bar, or "moi" in any article the user wrote.
- There also is 2 buttons on the top of the page that allow the user to either ask a review, or give one.

###### User flux
- This page is accessible at "http://127.0.0.1:8000/flux/user/_userid(int)_/", or by clicking "Flux personnalisé" on the side bar. The logged in user can also access it by clicking a pseudo on an article or the following-users management page. It displays only the posts the user, assiociated with the id in the search bar wrote.
- It also displays the username, and profil picture of the visited profil. The logged in user can follow or unfollow this profil.

###### Others
- The user can access a ticket flux by clicking on "Voir tous les avis" on any ticket. It displays the ticket, and the reviews published to answer this ticket.
- He can also access a book flux by clicking the name of the name of the book. It looks for every tickets that have the same title and author name, and query all the reviews associated, and displays everything ordered by date.


### Follow users features
###### From dedicated page
- The logged in user can manage the users he follows on a page accessible at "http://127.0.0.1:8000/search-users/follow/0/" or by clicking "Chercher des utilisateurs" in the side bar.
- On this page there is 3 features. The logged in user can see all the users he follows, and he can access their profils by clicking on their usernames, or unfollow them by clicking on the "unfollow" button. In an other div, he can see all the users he doesn't follow, access their profils by clicking on their usernames, and follow them by clicking the "follow" button. He can also search for a character chain and see all the user who have this chain in their usernames.

###### From user profil
- This is the same page than "User Flux". You can check the dedicated section for more infos.


### Profil management
###### Updating password
- This page is accessible at "http://127.0.0.1:8000/password-change/", or by clicking "Modifier mon mot de passe" on the side bar. It displays the form dadicated to change the password. It asks for the former password and the new one.
- Once done, the user is redirected on the public flux.

###### Updating profil picture
- This page is accessible at "http://127.0.0.1:8000/profil-pic-change/", or by clicking "Changer ma photo de profil" on the side bar. It displays the form dadicated to change the profil picture.
- Once done, the user is redirected on the public flux.

### Asking for reviews
###### Creating a ticket
- The user can access this page at "http://127.0.0.1:8000/ticket/create/" or by clicking on the "Demander un avis sur un livre" button. This button is displayed on every flux page, exept the "User flux".
- Once the user clicks on this, the user can enter some informations about the book. The title and the author are required. The description and image arn't.
- Once done, the user is redirected on the "Self flux".

###### Modifying a ticket
- The user can access this page at "http://127.0.0.1:8000/ticket/modify/_ticketid(int)_/" or by clicking on the "Modifier ma demande" link available on any ticket the user posted.
- It displays the form, with the actual informations, then the user can add/modify the data. 
- The user can also delete his ticket by clicking the "Supprimer" button on the bottom of the page.
- Once done, the user is redirected on the "Self flux" page.


### Posting reviews
###### Requested review
- Any user can add a review to any ticket. He can do it by simply clicking on the "Je donne mon avis" button on a ticket. This page is also accessible via the link "http://127.0.0.1:8000/review/_ticketid(int)/create/".
- Once on the page, the ticket is displayed, and the form to create a review below apears. The rating and headline are required, the body isn't. The rating will be display as stars on the review article once published.
- Once the form filled, and the "Publier" button is pressed, the user is redirected on the "Self flux".

###### Not requested review
- The user can access this page at "http://127.0.0.1:8000/review/ticket/create/" or by clicking on the "Donner son avis sur un livre" button. This button is displayed on every flux page, exept the "User flux".
- On this page, both the ticket create and review create forms are displayed. The user fill them with the same requirements than in the "Creating ticket" and "Requested review" sections.
- Once done, the program will save the ticket first, then the assiciated review, then redirects the user on the "Self flux".

###### Modifying a review
- The user can access this page at "http://127.0.0.1:8000/review/modify/_reviewid(int)_/" or by clicking on the "Modifier mon avis" link available on any ticket the user posted.
- The user can see the associated ticket, and modify the data of the review.
- He can also delete his review by simply clicking the "Supprimer mon avis" button at the bottom of the page.
- Once done, the user is redirected on the "Self flux" page.
