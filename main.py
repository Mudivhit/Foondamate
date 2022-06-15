import requests
import matplotlib.pyplot as graph


def api_data():
    try:
        response = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/").json()
        dates = []
        users = []
        for date in response:
            dates.append(date)
            users.append(response[date])

        return dates, users
    except:
        print("Oops, seems we could not reach the API, Please try again in a few moments")


def cli_interface():

    print("Welcome to the stats portal")
    date, users = api_data()
    date_range = [date[0], date[-1]]
    print("We have data for the following dates", date_range[0], "to",  date_range[1])
    while True:
        try:
            start = input("Input the start date (dd-mm-yyyy) : ")
            end = input("Input the end date   (dd-mm-yyyy) : ")
            start_index = date.index(start)
            end_index = date.index(end)

            dates_range = date[start_index:end_index + 1]
            data_range = users[start_index:end_index + 1]

            return dates_range, data_range
        except:
            print("Please select dates in the available range")


def grapher(labels, data):

    graph.xticks(range(len(data)), labels)
    graph.xlabel('Dates')
    graph.ylabel('Daily users')
    graph.title('Daily User stats')
    graph.bar(range(len(data)), data)
    graph.show()


if __name__ == '__main__':
    dates_info, date_data = cli_interface()
    grapher(dates_info, date_data)
