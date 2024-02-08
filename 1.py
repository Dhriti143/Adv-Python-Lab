#DHRITI SHAH 21BCP253
import os 

# Initialize an empty dictionary to store
#product id and its avg. ratings as key value pair
product = {} 
total_reviews=0
valid_reviews=0 

# Loop through each file in the input_directory
for filename in os.listdir():
    # Check if the file is a regular file and ends with ".txt" extension
    if filename.endswith(".txt") and (filename!="Summary.txt"):
        try:
            with open(filename, 'r') as file:
                print(file)
                for line in file:
                    print("\n",line)
                    total_reviews+=1
                    word = line.split(' ')
                    #Checking if there is rating or not
                    if(word[3]!='-'): 
                        key = word[1]
                        rating = float(word[3])
                        #Storing key-value pairs in dictionory
                        if key in product:
                            product[key]['total'] += rating
                            product[key]['count'] += 1
                        else:
                            product[key] = {'total': rating, 'count': 1}
                        #See if there is a review
                        comments = word[4]
                        comments = comments[0:2]
                        if(comments !='<>'): #<> means no review 
                            valid_reviews+=1
        except IOError:
            # Handle file read errors
            print(f"Error reading file: {filename}.Skipping it.")

# Write the summary data to the output_file
with open('Summary.txt', 'w') as s:
    s.write(f"Total reviews: {total_reviews}")
    s.write(f"\nValid_reviews reviews: {valid_reviews}")
    s.write(f"\nInvalid_reviews reviews: {total_reviews-valid_reviews}")
    #3 top rated product
    s.write(f"\nTop 3 rated Product:")
    for key,value in product.items():
        #calculating average rating of product
        v = round(value['total']/value['count'],2) 
        #updating value in dictionory and storing avg. ratings
        product[key] = v 
    #sort dictionary in descending order of average ratings using a lambda function.
    product1 = sorted(product.items(), key=lambda x:x[1], reverse = True) 
    for i in range(min(3,len(product1))):
        product_id, rating = product1[i]
        s.write(f"\nProduct ID:{product_id}, Rating:{rating}")