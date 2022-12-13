###########################################################
#  CSE 231 Project 7 
#  write functions to find max avg for 4 categories
#  Open 3 files of data 
#  Read each of the files of data
#  Display menu for choosing intended action
#  Depending on the chosen item, fine the maxavg for all 4 functions
#  Print the data and reprompt the selections (1-5)
#  Check errors with cases and reprompt for errors
###########################################################
GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
def open_file(s):
    ''' Prompts user to enter correct file name
        Value: String in place of the formatting 
        Return: file pointer of file
    '''
    while True: # looped for wrong file name entered
        filename=input('\nInput {} filename: '.format(s))
        try:
            fp= open(filename, 'r',encoding ="windows-1252") 
            return fp
        except FileNotFoundError: #if file not found print error
            print('\nError: No such file; please try again.')

def read_reviews(N,fp):
    ''' Reads the opened review file
        Value: file pointer from open file
        Return: list of sorted lists of tuples of ints of reviews
    '''
    L_reviews=[]
    N=int(N)
    for line in range(N+1): #N+1 for added users
        L_reviews.append([]) #append the empty list for later use
    for i in fp:
        L_split=i.split()
        userID=int(L_split[0]) 
        movieID=int(L_split[1])
        rating=int(L_split[2])
        tup=(movieID, rating)
        L_reviews[userID].append(tup) #append to empty list
        L_reviews[userID].sort()
    return L_reviews
            
def read_users(fp):
    ''' Reads the opened users file
        Value: file pointer from open file
        Return:List of tuples of the users
    '''
    master_list=[[]]
    for line in fp:
        line=line.strip()
        line=line.split("|")
        reviewer_id=line[0] #1st tup element
        age=int(line[1]) #2nd tup element
        gender=line[2] #3rd tup element
        occupation=line[3] #4th tup element
        tup=(age,gender,occupation) #make into a tup
        master_list.append(tup) #append the tup to the master list
    return master_list

def read_movies(fp): #TA assistance with line 73
    ''' Read the opened movies file
        Value: file pointer from open file
        Return: list of lists of movies
    '''
    L=[[]]
    for line in fp:
        line=line.strip().split("|")
        title=line[1]
        date=line[2]
        list_of_genres=line[5:]
        list_of_genres=[int(i) for i in list_of_genres]
        genres=[GENRES[i] for i, item in enumerate(list_of_genres) if item==1] #Grabs genre if item==1(True)
        L.append((title,date,genres))
    return L



def year_movies(year,L_movies): #TA assisted
    ''' Filter main movie list for year and return movie id list
        Value: int for year and movie tuple
        Return: Sorted list of ints of movie IDs
    '''
    L=[]
    for i in range(1,len(L_movies)):  
        try:
            day=L_movies[i]
            day=day[1]

            day=day[7:] #grabs the year
            date=int(day)
            if date== year:
                L.append(i) #append if the date equals the year
            else:
                continue
        except :
            continue
    return L


def genre_movies(genre,L_movies):
    ''' Filter main movie list for genre and return movie id list
        Value: string for genre and movie tuple
        Return: Sorted list of ints of movie IDs
    '''
    L=[]
    for x in range(1,len(L_movies)): #used range instead of enumerate
        genres=L_movies[x]
        genres=genres[2]
        for i in genres:
            if i==genre:
                L.append(x) #append the movie id according to genre if i=
            else:
                continue
    return L


def gen_users (gender, L_users, L_reviews): #TA assistance
    '''Filters main review list to find review of specific gender
       Value: gender string,List of tuples, and list of list of tups
       Return:review list as a list of list of tuples
    '''
    L=[]
    for i, tup in enumerate(L_users):
        if i==0:
            continue
        xx=tup[1] #gender index
        if xx == gender:
            L.append(L_reviews[i]) #append if xx equals the gender
    return L

        


          
def occ_users (occupation, L_users, L_reviews):
    '''Filters main review list to find review of specific occupation
       Value: occupation string,List of tuples, and list of list of tups
       Return:review list as a list of list of tuples
    '''
    L=[]
    for i, tup in enumerate(L_users):
        if i==0:
            continue
        xx=tup[2] #occupation index
        if xx == occupation:
            L.append(L_reviews[i]) #append if xx equals that occupation
    return L

def highest_rated_by_movie(L_in,L_reviews,N_movies): #HELPED BY TA**
    '''calculates the average rating for the reviews in L_reviews
       Value: list of ints and list of list of tuple for reviews
       Return: a list of the highest average rated movies and the 
       highest average
    '''
    tot=[0]*len(L_in)
    n=[0]*len(L_in)
    av=[0]*len(L_in)
    for i in range(len(L_in)):
        for p in L_reviews:
            if p!=[]:
                for m in p:
                    if L_in[i]==m[0]:
                        tot[i]+=m[1]
                        n[i]+=1
    for i in range(len(L_in)):
        av[i]= round(tot[i]/n[i],2)
    maximumms=[]
    maximum= max(av)
    for i in range(len(av)):
        # if av[i]>maximum:
        #     maximum=av[i]
        #     maximumms=[]
        if av[i]==maximum:
            maximumms.append(L_in[i])
    return maximumms, maximum


             
def highest_rated_by_reviewer(L_in,N_movies): # Helped by Zane and Juan**
    '''calculates the average rating for movies by specific users
       Value:list of list of tuples and int for the number of movies
       Return:a list of the highest average rated movies and the
       highest average
    '''
    sums=[0]*(N_movies)
    counts=[0]*(N_movies)
    for listt in L_in:
        for movieID,rating in listt:
            #if rating==0 or movieID==0:
            #    continue
            sums[movieID-1]+=rating
            counts[movieID-1]+=1
    maxavg=-100
    movieavg=[]
    average=0
    for i in range(N_movies):
        if counts[i]!=0:
            average= round((sums[i]/counts[i]),2)
        else:
            average=0

        if average>maxavg:
            maxavg=average
        movieavg.append(average)

    maxavg = max(movieavg)
    
    

    toprating=[]
    for i, avg in enumerate(movieavg):

        if maxavg==avg:
            toprating.append(i+1)

    return toprating, maxavg

        
def main():
    n=0
    dp=open_file('users')
    fp=open_file('reviews')
    mp=open_file('movies')
    user_list=read_users(dp)
    n=len(user_list) #need n from the user list to use as a parameter for read reviews
    review_list=read_reviews(n,fp)
    movie_list=read_movies(mp)
    print(MENU)
    user_input=int(input('\nSelect an option (1-5): '))
    while True:
        if user_input==1:
            yearput=int(input('\nInput a year: '))
            while True:
                if 1930<=yearput<=1998: #checks if in between the given years
                    movie=year_movies(yearput, movie_list)
                    rating, maxavg =highest_rated_by_movie(movie,
                    review_list,0)
                    print('\nAvg max rating for the year is:', round(maxavg, 2)) #or use 1 var and index to 
                    [1]
                    for x in rating:
                        print(movie_list[x][0]) #prints movie with the avgs
                    user_input=int(input('\nSelect an option (1-5): '))#after completed test ask input again
                    break
                else:
                    print("\nError in year.")
                    yearput=int(input('\nInput a year: ')) #reprompting if invalid year entered
                    continue
                continue
        elif user_input==2:
            print('\nValid Genres are: ',GENRES)
            genre_input= input('Input a genre: ').capitalize() #lowercase all then capitalize 1st letter
            while True:
                if genre_input in GENRES: 
                    gen=genre_movies(genre_input,movie_list)
                    rat=highest_rated_by_movie(gen,review_list,0)
                    print('\nAvg max rating for the Genre is:', round(rat[1],2))
                    for i in rat[0]:# basically using the Same formatting of code for option 1
                        print(movie_list[i][0])
                    user_input=int(input('\nSelect an option (1-5): '))
                    break
                else:
                    print("\nError in genre.")
                    genre_input= input('Input a genre: ').capitalize()
                    continue
                continue

                
                
                    
        
        elif user_input==3:
            genderput=input('\nInput a gender (M,F): ')
            while True:
                if genderput.upper()== 'M' or genderput.upper()== 'F': #convert input to caps
                    callgen=gen_users(genderput.upper(), user_list, 
                    review_list)
                    callavg=highest_rated_by_reviewer(callgen,len(movie_list)) #2nd pararmeter Nmovies len listt 

                    print('\nAvg max rating for the Gender is:',callavg[1])
                    for i in callavg[0]:
                        print(movie_list[i][0]) #same as all other options
                    user_input=int(input('\nSelect an option (1-5): '))
                    break
                else:
                    print("\nError in gender.")
                    genderput=input('\nInput a gender (M,F): ')
                    continue
                continue


        elif user_input==4:
            print('\nValid Occupatipns are: ',OCCUPATIONS)
            occ_input= str(input('Input an occupation: ')).lower()# .lower stated in instructions for the list
            while True:
                if occ_input in OCCUPATIONS:
                    callocc=occ_users(occ_input, user_list,review_list)
                    call_avg=highest_rated_by_reviewer(callocc,len(movie_list))
                    print('\nAvg max rating for the occupation is:',round(call_avg[1],2))
                    for i in call_avg[0]:
                        print(movie_list[i][0]) #same as the others
                    user_input=int(input('\nSelect an option (1-5): '))
                    break
                else:
                    print("\nError in occupation.")
                    occ_input= input('Input an occupation: ').lower()
                    continue
                continue
        elif user_input==5:
            break #if 5 entered, stop the program
        else:
            print("\nError: not a valid option.") #elsewise, print error and reprompt
            user_input=int(input('\nSelect an option (1-5): '))
            continue
  

if __name__ == "__main__":
    main()
                                           
