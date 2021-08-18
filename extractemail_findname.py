import re
import pandas as pd

def extract_email(s) :
    find_emails = "([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})"
    emails = re.findall(find_emails, s)
    return emails

def find_name_from_email(s,emails) :
    tokens = s.split()
    name = []
    # print(tokens)

    for token in tokens :
        for mail in emails :
            if(token.lower() in mail[0].lower() and len(token)>1):
                name.append(token)
    return name

def unique(list1):
 
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    
    return unique_list

def find_neighbours(tokens,names) :
    name_dict = {}
    for i in range(len(tokens)) :
        for name in names :
            ls = []
            if tokens[i] == name :
                if i==0 :
                    ls.append(tokens[i+1])
                elif (i==(len(tokens)-1)) :
                    ls.append(tokens[i-1])
                else :
                    ls.append(tokens[i+1])
                    ls.append(tokens[i-1])
                name_dict[name]=ls
    return name_dict

def check_in_dataset(name_dict,names):
    df = pd.read_csv("final_csv_together.csv")

    for name in names :
        for val in name_dict[name] :
            if val.lower() not in str(df.name) :
                name_dict[name].remove(val)
    return name_dict

def find_names_from_dict(name_dict) :
    ls = []
    for key in name_dict :
        ls.append(key)
        for val in name_dict[key] :
            ls.append(val)
    unique_list= unique(ls)

    final_name = ' '.join(unique_list).upper()
    return final_name

def extract_name(s,names) : 
    tokens = s.split()

    name_dict = find_neighbours(tokens,names)
    clean_dict = check_in_dataset(name_dict,names)

    final_name = find_names_from_dict(name_dict)
    return final_name


def main() :

    s = """AMAL Puthur GANESH
Contact
amalganesh4u@gmail.com
7356529545
Parambath house Mottammal P. O
Kannapuram, kannur 670331"""

    emails = extract_email(s)

    if emails : 
        candidates = find_name_from_email(s,emails)
        name = extract_name(s,candidates)
        print(name)
    


if __name__ == "__main__":
    main()