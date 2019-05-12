import json
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

def contcatinate_steps(solution_json):
    descp = ''

    for step in solution_json:
        descp = descp + solution_json[step]

    return descp

def tokenize_data(descp):
    return word_tokenize(descp)

def clean_data(descp):
    #Removing punctuations
    descp = descp.translate(str.maketrans('', '', string.punctuation))
    #Tokenizing data
    tokens = tokenize_data(descp)
    #Changing to lower case
    tokens = [w.lower() for w in tokens]
    #Stemming words
    porter = PorterStemmer()
    tokens = [porter.stem(w) for w in tokens]

    clean_data = []
    stop_words = stopwords.words('english')

    for tkn in tokens:
        if(tkn != stop_words):
            clean_data.append(tkn)

    return clean_data

def reorder_data(data_obj):
    solutions_data = data_obj  # json.loads(open(file_name).read())
    reordered_data = []

    for sol in solutions_data:
        reordered_solution = {}
        reordered_solution['solutionID'] = sol['solutionID']
        reordered_solution['descp'] = contcatinate_steps(sol['solution'])

        reordered_data.append(reordered_solution)

    #Reordered ordered is in the following format
    # [
    #     {
    #         'solutionID': 1.0, 
    #         'descp': 'There are muliple configurations to be checked to understand why push notification not reached to ios device even though the status was submitted.First of all check whether user configured same bundle identifier The push certificate will be based on the bundle identifier and same needs to be configured in kms console.in the application. You can find the bundle identifier in your provision profileIf above step is correct we need to confirm whether you used correct profile while building the application in xcode. If you are using developer certificate then you have to use developer profile or if distribution certificate then user has to build the application using distribution profileIf above step is correct then we need to verify by using mobile sim data instead of using corporate wifi. Sometime corporate wifi will block the push notification. To rule out any wifi network restrictions.If still not receiving the push notification, need to recreate the profile and certificate. And need to verify again by sending notifications.Please follow the link to create the profile and push certificates'
    #     }
    # ]

    for solution in reordered_data:
        solution['descp'] = clean_data(solution['descp'])

    print(reordered_data)

def main():
    data_obj = [{'solutionID': 1.0, 'solution': {'step1': 'There are muliple configurations to be checked to understand why push notification not reached to ios device even though the status was submitted.First of all check whether user configured same bundle identifier The push certificate will be based on the bundle identifier and same needs to be configured in kms console.in the application. You can find the bundle identifier in your provision profile',
                                                 'step2': 'If above step is correct we need to confirm whether you used correct profile while building the application in xcode. If you are using developer certificate then you have to use developer profile or if distribution certificate then user has to build the application using distribution profile', 'step3': 'If above step is correct then we need to verify by using mobile sim data instead of using corporate wifi. Sometime corporate wifi will block the push notification. To rule out any wifi network restrictions.', 'step4': 'If still not receiving the push notification, need to recreate the profile and certificate. And need to verify again by sending notifications.', 'step5': 'Please follow the link to create the profile and push certificates'}}]
    solutions = reorder_data(data_obj)


if __name__ == "__main__":
    main()
