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
- Once you are logged in, you are redirected on the pubic flux, and some options are available to you. Let's explore them.  

## Using the website
#### Differents flux
- The different types of flux select which tickets and reviews to display.    
- On each tickets, you can add a review, access the flux of the corresponding ticket, access the flux of the corresponding book, or access the profil of the poster. It displays all the informations conserning the book that the poster gave. If you are the poster, you can access your profil, or the modifying form to update or delete your ticket.    
- On each reviews, you can add yours, access the flux of the corresponding book, access the profil of the related ticket's poster, or the profil of the review poster. If you are the poster, you can access your profil, or the modifying form to update or delete your review. It displays Some informations about the book (title, authore, cover if any), and the grade and comments writen by the poster.    
- All of the differents flux are paginated with a limit of 5 article per page. The pagination is displayed only if the number of article is above this limit.    
###### Public flux
- On this page is accessible at "http://127.0.0.1:8000/flux", or by clicking "Flux publique" on the side bar. You can see all the tickets and reviews posted by the community order by date. The most recent first.
- You also have 2 buttons on the top of the page that allow you to either ask a review, or give one.    
###### Custom flux
- This page is accessible at "http://127.0.0.1:8000/flux/perso/", or by clicking "Flux personnalisé" on the side bar. It displays 3 types of datas. First : the posts (tickets and reviews) posted by people you follow, second, your own posts and finaly the reviews that answer to your tickets. The program order all this by date.
- You also have 2 buttons on the top of the page that allow you to either ask a review, or give one.   
###### Self flux
- This page is accessible at "http://127.0.0.1:8000/flux/self/", or by clicking "Flux personnalisé" on the side bar. It displays only the post you wrote. You can also access it by clicking your pseudo in the side bar, or "moi" in any article you wrote.
- You also have 2 buttons on the top of the page that allow you to either ask a review, or give one.   
###### User flux
- This page is accessible at "http://127.0.0.1:8000/flux/user/_int_/", or by clicking "Flux personnalisé" on the side bar. You can also access it by clicking a pseudo on an article or the following management page. It displays only the post the user, assiociated with the id in the search bar wrote.
- It also displays the username, and profil picture of the visited profil. As user, you can follow or unfollow this profil.
###### Others
(Ticket, book)
- You can access a ticket flux by clicking on "Voir tous les avis" on any ticket. It display the ticket, and the reviews published to answer this ticket.
- You can access a book flux by clicking the name of the name of the book. It look for every tickets that have the same title and author name, and query all the reviews assiciated, and displays everything ordered by date.

#### Follow users features
###### From dedicated page
###### From user profil

#### Profil management
###### Updating password
###### Updating profil picture

#### Asking for reviews
###### Creating a ticket
###### Modifying a ticket

#### Posting reviews
###### Requested review
###### Not requested review
###### Modifying a review
