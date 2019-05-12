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
    # Removing punctuations
    descp = descp.translate(str.maketrans('', '', string.punctuation))
    # Tokenizing data
    tokens = tokenize_data(descp)
    # Changing to lower case
    tokens = [w.lower() for w in tokens]
    # Stemming words
    porter = PorterStemmer()
    #tokens = [porter.stem(w) for w in tokens]

    clean_data = []
    stop_words = stopwords.words('english')

    for tkn in tokens:
        if(tkn not in stop_words):
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

    # Reordered ordered is in the following format
    # [
    #     {
    #         'solutionID': 1.0,
    #         'descp': 'There are muliple configurations to be checked to understand why push notification not reached to ios device even though the status was submitted.First of all check whether user configured same bundle identifier The push certificate will be based on the bundle identifier and same needs to be configured in kms console.in the application. You can find the bundle identifier in your provision profileIf above step is correct we need to confirm whether you used correct profile while building the application in xcode. If you are using developer certificate then you have to use developer profile or if distribution certificate then user has to build the application using distribution profileIf above step is correct then we need to verify by using mobile sim data instead of using corporate wifi. Sometime corporate wifi will block the push notification. To rule out any wifi network restrictions.If still not receiving the push notification, need to recreate the profile and certificate. And need to verify again by sending notifications.Please follow the link to create the profile and push certificates'
    #     }
    # ]

    for solution in reordered_data:
        solution['descp'] = clean_data(solution['descp'])

    return reordered_data

def main():
    data_obj = [
        {
            "solutionID": 1,
            "solution": {
                "step1": "There are muliple configurations to be checked to understand why push notification not reached to ios device even though the status was submitted.First of all check whether user configured same bundle identifier The push certificate will be based on the bundle identifier and same needs to be configured in kms console.in the application. You can find the bundle identifier in your provision profile",
                "step2": "If above step is correct we need to confirm whether you used correct profile while building the application in xcode. If you are using developer certificate then you have to use developer profile or if distribution certificate then user has to build the application using distribution profile",
                "step3": "If above step is correct then we need to verify by using mobile sim data instead of using corporate wifi. Sometime corporate wifi will block the push notification. To rule out any wifi network restrictions.",
                "step4": "If still not receiving the push notification, need to recreate the profile and certificate. And need to verify again by sending notifications.",
                "step5": "Please follow the link to create the profile and push certificates"
            }
        },
        {
            "solutionID": 2,
            "solution": {
                "step1": "There would be only 1 reason for showing the status as submitted but notification not reached to android device, i.e the fire wall restrictions or slow network and internet connectivity issues. You have to white list the domains mentioned in the Corporate fire wall settings of the below link. http://docs.kony.com/konylibrary/messaging/kms_console_installer_manual_guide-windows/Default.htm#Prerequisites.htm%3FTocPath%3D_____4"
            }
        },
        {
            "solutionID": 3,
            "solution": {
                "step1": "When you see the message status as rejected under KMS console, just hover the browser over the message and you will see a popup message like Not registered or mismatch sender Id.",
                "step2": "Not Registered : Even though the subscription status and cloud status are active at the moment, it is not for sure. Suppose if you uninstall the application from device right away the subscription status won’t become inactive right away. Its because this status will be fetched by KMS once in 24 hours by connecting to its corresponding cloud(GCM,FCM or APNS). So KMS will still show it as active device and you will try to send the push. When KMS deliver this message GCM or APNS they will reject saying this device is not a registered device. So inorder to resolve this, please register again from the application followed by subscription",
                "step3": "Mismatch Sender ID:It means that the GCM or FCM server key configured in the KMS console application is of some other google project but not of the project whose sender id you used for registration of google cloud. So giving the appropriate server key would resolve this issue.",
                "step4": "Suppose if a push message to IOS device was rejected by APNS, it means that there are restrictions at firewall level like proxy configurations. So please check whether below firewall settings are enabled or not.Please note that if you a firewall proxy, then you should enable the socks protocol for that proxy server, else apple wouldn’t accept the requests. So this is a restriction from apple itself.",
                "step5": "Couple of status and their meaning. 1)Rejected- It means the KMS requested the corresponding push manufacturer clouds like GCM,FCM,APNS,WNS and MPNS, but they have rejected your requests due to variant reasons. 2)Cancelled- Kony MobileFabric Messaging cancelled to sent the message before it reached the respective cloud of designated platform.3)Undelivered- Kony MobileFabric Messaging tried sending the message, but it was undelivered to the respective cloud of the designated platform due to any possible reasons. For example the, GCM key was missing for Google cloud.NotAttempted- Kony Messaging did not try sending the message because no subscribers  for the chosen. You will see this for the scheduled push messages, where users will unsubscribe after admin had scheduled the push messages."
            }
        },
        {
            "solutionID": 4,
            "solution": {
                "step1": "1)401 : Some times when accessed the kms api, you will get the Authentication failed in the response body and status code will be 401. It means that you are not passing authorization data in the headers (most probably tokens). Authentication for kms is of two types. 1.Basic Auth(Database Authentication). 2.MBAAS Auth(Kony REST service Authentication).To understand which authentication to use please follow the below link.http://docs.kony.com/konylibrary/messaging/engagement_api_guide/Content/APIs_for_Kony_Messaging_Services/Authentication_API.htm#On2"
            }
        },
        {
            "solutionID": 5,
            "solution": {
                "step1": "1)403 :you can see kms rest API’s failing with 403, it means that the request to the KMS came from another domain and kms by default KMS  won’t allow the cross domain requests. So in order resolve this and proceed further follow the below steps. a)Go to kms console. b)Select configuration-->General. c)Under SECURITY section you will find the ‘Allow Cross Domains Access’ check box. d)Beneath the check box there will be a text box and fill it with character ‘*’ and save"
            }
        },
        {
            "solutionID": 6,
            "solution": {
                "step1": "1)404 :It means the REST API using  does not exists in the KMS web directory and you can go to API help section in the kms console and check all the REST API’s provided by kms"
            }
        },
        {
            "solutionID": 7,
            "solution": {
                "step1": "1.ANDROID : When you go to KMS APPSettingsAndroid and configured the GCM or FCM project server key under the GCM/FCM Authorization Key and cliked on test connectivity, you are getting the “Android GCM/FCM cloud connection validation failed.The first reason could be restrictions at firewall. Please make sure that access to ‘fcm.googleapis.com’ is enabled at firewall. Moreover there are other firewall settings too as mentioned in the link below.http://docs.kony.com/konylibrary/messaging/kms_console_installer_manual_guide-windows/Default.htm#Prerequisites.htm%3FTocPath%3D_____4.The second reason could be that the given GCM server key is not appropriate, so cross verify the given server key with your google developer project server key."
            }
        },
        {
            "solutionID": 8,
            "solution": {
                "step1": "1.IOS : When you go to KMS App Settings Apple and uploaded the p12 certificate and click on “Test connectivity with cloud”, you will get the “Apple cloud Connection Test failed”.The first reason would be may be due to the uploading of development to production section or uploading the production certificate to development section shown below.There may be firewall restrictions to access the apple cloud. So ensure all the settings in the below link were enabled. The foremost thing is that if there is a firewall proxy server, then you must and should enable the socks protocol for the proxy server, it’s a restriction from apple itself.   http://docs.kony.com/konylibrary/messaging/kms_console_installer_manual_guide-windows/Default.htm#Prerequisites.htm%3FTocPath%3D____",
                "step2": "If there is a proxy enabled, you have to configure the same details in the configureresource.properties under KPNS/WEB-INF/classes of your web directory. These proxy key’s are commeted by default, so uncomment and fill the values and restart the server. Sample configresource.properties file is shown below. http://docs.kony.com/konylibrary/messaging/kms_console_installer_manual_guide-windows/Default.htm#Setup_KPNS.htm#ConfigResource.pro%3FTocPath%3DInstall%2520and%2520Configure%2520Engagement%2520Services%7CSetup%2520Engagement%2520Services%7C_____1",
                "step3": "If the issue still exists, please check the configureresource.properties under KPNS/WEB-INF/classes whether any commented property still exists in the KPNSDB database schema. The corresponding database table is “config_resources”. If the commented values still exists in the database, try restarting the server. If they still exists, manually delete the entire record from the table and it would resolve the issue.",
                "step4": " You can do the below commands to check the connectivity to apple cloud.1)WINDOW server:tracert. 2)linux server:traceroute"
            }
        },
        {
            "solutionID": 9,
            "solution": {
                "step1": "Android : we are not giving any workarounds for this issue, as this already taken by L3 and under the brain storm by people. The workarounds will be given by the SME only after validating the user environment, else we would end up in issues"
            }
        },
        {
            "solutionID": 10,
            "solution": {
                "step1": "Duplicate messages will be received to IOS devices in only 1 case i.e the scheduled messages through campaigns or when did the bulk push through CSV using bulk push API",
                "step2": "Bulk push: When the push entries are reciprocated in the same CSV file , the kms will fetch the entire list and will create entries under the ‘messageentry’ table and then it will pick the entries from the same table and will push them to corresponding  push clouds(GCM,APNS…etc) at an average frequency of 50 to 60 messages/sec. If there are any duplicate entries in the CSV file, there is a very high probability for your device to receive the back to back messages with in an interval of 1 second or even less. So make sure you have not sending the same message to same device multiple times under the same csv file.",
                "step3": "Scheduled Messages through campaigns: When you scheduled a campaign, the kms will first fetch the subscribers who will fall under the constraints mentioned in the campaign and will create the message entries for those subscribers in the ‘messageentry’ table. For the entries in this table you will have the unique message id under the column ‘id’.  So if a duplicate push message is received for the device, please follow the below steps. 1. From the kms console-->subscribers page get the ‘KSID” of that device registered to your KMS app. 2.2.Go to the ‘messageentry’ table and run the sql query with your ‘user defined message’ and the retrieved ‘KSID’ Select * from messagerequest where message=’your message’ and subscription=’KSID’;. 3. The above query will definitely more than 1 record and it means that you only configured duplicate messages. If you want to counter check you can see the values of ‘startTimestamp’ value of the result records and they would be same for sure."
            }
        }
    ]
    solutions = reorder_data(data_obj)

    print(solutions)


if __name__ == "__main__":
    main()
